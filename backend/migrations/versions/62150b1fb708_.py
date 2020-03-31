"""empty message

Revision ID: 62150b1fb708
Revises: c895d9c662e9
Create Date: 2020-03-31 10:03:08.672317

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '62150b1fb708'
down_revision = 'c895d9c662e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource', sa.Column('covid19_categories', postgresql.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resource', 'covid19_categories')
    # ### end Alembic commands ###
