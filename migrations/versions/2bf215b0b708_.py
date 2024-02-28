"""empty message

Revision ID: 2bf215b0b708
Revises: 
Create Date: 2024-02-28 10:38:37.751123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bf215b0b708'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ca_name', sa.String(length=128), nullable=False),
    sa.Column('ca_description', sa.String(length=250), nullable=False),
    sa.Column('ca_uid', sa.String(length=128), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###