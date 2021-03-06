"""empty message

Revision ID: 564e91456850
Revises: 95839040477b
Create Date: 2019-02-04 16:19:25.511348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '564e91456850'
down_revision = '95839040477b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('education_questionnaire', sa.Column('dependent_placement', sa.String(), nullable=True))
    op.add_column('education_questionnaire', sa.Column('placement_other', sa.String(), nullable=True))
    op.add_column('education_questionnaire', sa.Column('school_type', sa.String(), nullable=True))
    op.add_column('education_questionnaire', sa.Column('self_placement', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('education_questionnaire', 'self_placement')
    op.drop_column('education_questionnaire', 'school_type')
    op.drop_column('education_questionnaire', 'placement_other')
    op.drop_column('education_questionnaire', 'dependent_placement')
    # ### end Alembic commands ###
