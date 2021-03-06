"""add # of songs to artist

Revision ID: feee4f25dd19
Revises: 06489dc1a07f
Create Date: 2022-05-16 21:04:38.684743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feee4f25dd19'
down_revision = '06489dc1a07f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number_of_songs', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.drop_column('number_of_songs')

    # ### end Alembic commands ###
