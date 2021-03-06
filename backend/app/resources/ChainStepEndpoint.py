import datetime

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful
from flask import request
from sqlalchemy.exc import IntegrityError

from app import RestException, db, auth
from app.model.chain_step import ChainStep
from app.model.questionnaires.chain_session_step import ChainSessionStep
from app.model.role import Permission
from app.schema.chain_step_schema import ChainStepSchema
from app.wrappers import requires_permission


class ChainStepEndpoint(flask_restful.Resource):
    """SkillSTAR Chain Step"""
    schema = ChainStepSchema()

    def get(self, chain_step_id):
        chain_step = db.session.query(ChainStep).filter_by(id=int(chain_step_id)).first()
        if chain_step is None:
            raise RestException(RestException.NOT_FOUND)
        return self.schema.dump(chain_step)

    @auth.login_required
    @requires_permission(Permission.edit_study)
    def put(self, chain_step_id):
        """Modifies an existing Chain Step, or adds one if none exists."""
        request_data = request.get_json()
        instance = db.session.query(ChainStep).filter_by(id=chain_step_id).first()
        try:
            if instance is None:
                # New step
                updated_step = self.schema.load(request_data)
                updated_step.name = 'toothbrushing_' + f'{(updated_step.id + 1):02}'
            else:
                updated_step = self.schema.load(request_data, instance=instance, session=db.session)
        except Exception as e:
            raise RestException(RestException.INVALID_OBJECT, details=e)
        updated_step.last_updated = datetime.datetime.utcnow()
        db.session.add(updated_step)
        db.session.commit()
        return self.schema.dump(updated_step)

    @auth.login_required
    @requires_permission(Permission.edit_study)
    def delete(self, chain_step_id):
        """Deletes existing Chain Step, but only if there are no Chain Session Steps that refer to it."""
        chain_session_step = db.session\
            .query(ChainSessionStep)\
            .filter(ChainSessionStep.chain_step_id == chain_step_id)\
            .first()

        if chain_session_step is not None:
            raise RestException(RestException.CAN_NOT_DELETE, details='Cannot delete a Chain Step that has Chain Session data referring to it.')

        try:
            db.session.query(ChainStep).filter_by(id=chain_step_id).delete()
            db.session.commit()
        except IntegrityError as error:
            raise RestException(RestException.CAN_NOT_DELETE)
        return


class ChainStepListEndpoint(flask_restful.Resource):
    """SkillSTAR Chain Steps"""
    schema = ChainStepSchema(many=True)

    def get(self):
        chain_steps = db.session.query(ChainStep).all()
        if chain_steps is None:
            raise RestException(RestException.NOT_FOUND)

        sorted_steps = sorted(chain_steps, key=lambda chain_step: chain_step.id)
        return self.schema.dump(sorted_steps)
