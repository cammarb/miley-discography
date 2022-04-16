"""remove time length

Revision ID: 44fba5de3f3c
Revises: b33b469c7d8f
Create Date: 2022-04-16 14:38:36.734700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44fba5de3f3c'
down_revision = 'b33b469c7d8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('album', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_length', sa.String(), nullable=True))

    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.drop_column('length')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.add_column(sa.Column('length', sa.TIME(), nullable=False))

    with op.batch_alter_table('album', schema=None) as batch_op:
        batch_op.drop_column('total_length')

    # ### end Alembic commands ###
