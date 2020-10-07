"""empty message

Revision ID: b1b7d9b47b56
Revises: fcd6c141f060
Create Date: 2020-08-21 16:37:54.608704

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b1b7d9b47b56'
down_revision = 'fcd6c141f060'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('registration_questionnaire', sa.Column('participant_id', sa.Integer(), nullable=True))
    op.create_foreign_key('registration_questionnaire_participant_id_fkey', 'registration_questionnaire', 'stardrive_participant', ['participant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('registration_questionnaire_participant_id_fkey', 'registration_questionnaire', type_='foreignkey')
    op.drop_column('registration_questionnaire', 'participant_id')
    # ### end Alembic commands ###