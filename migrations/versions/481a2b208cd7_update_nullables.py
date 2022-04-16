"""update nullables

Revision ID: 481a2b208cd7
Revises: c099b84b4879
Create Date: 2022-04-16 14:44:40.041121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '481a2b208cd7'
down_revision = 'c099b84b4879'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('album', schema=None) as batch_op:
        batch_op.alter_column('is_live',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.alter_column('is_ep',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('album', schema=None) as batch_op:
        batch_op.alter_column('is_ep',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('is_live',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    # ### end Alembic commands ###
