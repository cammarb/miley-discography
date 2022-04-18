"""remove order in SongTto

Revision ID: 9356bcff9bb5
Revises: 481a2b208cd7
Create Date: 2022-04-17 20:04:58.572198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9356bcff9bb5'
down_revision = '481a2b208cd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song_to_artist', schema=None) as batch_op:
        batch_op.drop_column('order')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song_to_artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
