"""empty message

Revision ID: 3acf6852c1f2
Revises: 
Create Date: 2024-04-05 19:56:29.527354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3acf6852c1f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teller',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('t_fullname', sa.String(length=128), nullable=False),
    sa.Column('t_username', sa.String(length=128), nullable=False),
    sa.Column('t_mobile', sa.String(length=128), nullable=False),
    sa.Column('t_address', sa.String(length=128), nullable=False),
    sa.Column('t_email', sa.String(length=128), nullable=False),
    sa.Column('t_password', sa.String(length=128), nullable=False),
    sa.Column('t_city', sa.String(length=128), nullable=False),
    sa.Column('t_uid', sa.String(length=128), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teller')
    # ### end Alembic commands ###