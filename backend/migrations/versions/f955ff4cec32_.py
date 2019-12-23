"""empty message

Revision ID: f955ff4cec32
Revises: 771d1705b043
Create Date: 2019-12-09 14:05:39.233075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f955ff4cec32'
down_revision = '771d1705b043'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource', sa.Column('video_link', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resource', 'video_link')
    # ### end Alembic commands ###