"""empty message

Revision ID: 6366de224eec
Revises: 2fd0ab60fe3a
Create Date: 2019-03-01 09:53:05.240155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6366de224eec'
down_revision = '2fd0ab60fe3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('home_self_questionnaire', 'self_living_situation',
                    existing_type=sa.VARCHAR(),
                    type_=sa.ARRAY(sa.VARCHAR()),
                    existing_nullable=True,
                    postgresql_using='array[self_living_situation]'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('home_self_questionnaire', 'self_living_situation',
               existing_type=sa.ARRAY(sa.String(), dimensions=10),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    # ### end Alembic commands ###
