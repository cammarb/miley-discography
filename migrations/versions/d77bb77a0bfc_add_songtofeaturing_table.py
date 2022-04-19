"""add SongToFeaturing table

Revision ID: d77bb77a0bfc
Revises: f38642c0a42c
Create Date: 2022-04-17 20:57:52.017466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd77bb77a0bfc'
down_revision = 'f38642c0a42c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song_to_featuring',
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('featuring_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['featuring_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['song.id'], ),
    sa.PrimaryKeyConstraint('song_id', 'featuring_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song_to_featuring')
    # ### end Alembic commands ###