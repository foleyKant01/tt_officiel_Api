"""empty message

Revision ID: 9c854b4281db
Revises: 
Create Date: 2024-03-20 12:13:40.766959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c854b4281db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bu_city', sa.String(length=128), nullable=False))
        batch_op.add_column(sa.Column('bu_pic1', sa.String(length=128), nullable=False))
        batch_op.add_column(sa.Column('bu_pic2', sa.String(length=128), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('business', schema=None) as batch_op:
        batch_op.drop_column('bu_pic2')
        batch_op.drop_column('bu_pic1')
        batch_op.drop_column('bu_city')

    # ### end Alembic commands ###
