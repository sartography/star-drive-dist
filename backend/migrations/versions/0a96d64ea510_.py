"""empty message

Revision ID: 0a96d64ea510
Revises: 68e16832d52a
Create Date: 2020-01-24 14:29:35.666144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a96d64ea510'
down_revision = '68e16832d52a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('study', sa.Column('results_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('study', 'results_url')
    # ### end Alembic commands ###
