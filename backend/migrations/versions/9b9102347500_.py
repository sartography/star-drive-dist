"""empty message

Revision ID: 9b9102347500
Revises: 7ede01846a31
Create Date: 2019-08-14 12:26:40.368422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b9102347500'
down_revision = '7ede01846a31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('study', sa.Column('image_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('study', 'image_url')
    # ### end Alembic commands ###
