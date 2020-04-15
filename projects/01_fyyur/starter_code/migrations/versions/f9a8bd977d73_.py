"""empty message

Revision ID: f9a8bd977d73
Revises: 17ba9ee63358
Create Date: 2020-04-15 09:33:54.770520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9a8bd977d73'
down_revision = '17ba9ee63358'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('address', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'address')
    # ### end Alembic commands ###
