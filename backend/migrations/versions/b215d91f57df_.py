"""empty message

Revision ID: b215d91f57df
Revises: 5cd8941ace02
Create Date: 2021-05-11 16:23:14.606903

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b215d91f57df'
down_revision = '5cd8941ace02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usermeta', sa.Column('last_updated', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usermeta', 'last_updated')
    # ### end Alembic commands ###
