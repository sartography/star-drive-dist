import enum

from sqlalchemy import func

from app import db
from app.model.participant_relationship import Relationship


class UserMeta(db.Model):
    __tablename__ = 'usermeta'
    __label__ = "User Meta Info"
    id = db.Column(db.Integer, db.ForeignKey('stardrive_user.id'), primary_key=True)
    last_updated = db.Column(db.DateTime(timezone=True), default=func.now())
    self_participant = db.Column(db.Boolean)
    self_has_guardian = db.Column(db.Boolean)
    guardian = db.Column(db.Boolean)
    guardian_has_dependent = db.Column(db.Boolean)
    professional = db.Column(db.Boolean)
    interested = db.Column(db.Boolean)

    def get_relationship(self):
        if self.self_participant:
            return None if self.self_has_guardian else Relationship.self_participant.name
        if self.guardian and self.guardian_has_dependent:
            return Relationship.self_guardian.name
        if self.professional:
            return Relationship.self_professional.name
        # Lower Precedence Relationships
        if self.guardian and not self.guardian_has_dependent:
            return Relationship.self_interested.name
        if self.interested:
            return Relationship.self_interested.name
        return ''

