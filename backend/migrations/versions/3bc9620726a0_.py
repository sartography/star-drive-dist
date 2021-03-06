"""empty message

Revision ID: 3bc9620726a0
Revises: 199912fae9ba
Create Date: 2019-02-04 11:29:01.942956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bc9620726a0'
down_revision = '199912fae9ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stardrive_user', 'last_name')
    op.drop_column('stardrive_user', 'first_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stardrive_user', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('stardrive_user', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
