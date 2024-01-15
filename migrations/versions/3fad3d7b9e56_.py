"""empty message

Revision ID: 3fad3d7b9e56
Revises: 
Create Date: 2024-01-15 14:09:03.915100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fad3d7b9e56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bu_uid', sa.String(length=128), nullable=False))

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ca_uid', sa.String(length=128), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('ca_uid')

    with op.batch_alter_table('business', schema=None) as batch_op:
        batch_op.drop_column('bu_uid')

    # ### end Alembic commands ###
