"""add featuring to SongToArtist model

Revision ID: 12a9c54e3bfa
Revises: 9356bcff9bb5
Create Date: 2022-04-17 20:07:55.873344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12a9c54e3bfa'
down_revision = '9356bcff9bb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song_to_artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('featuring', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song_to_artist', schema=None) as batch_op:
        batch_op.drop_column('featuring')

    # ### end Alembic commands ###
