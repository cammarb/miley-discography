"""remove ft column

Revision ID: f38642c0a42c
Revises: 12a9c54e3bfa
Create Date: 2022-04-17 20:55:24.998710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f38642c0a42c'
down_revision = '12a9c54e3bfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song_to_artist', schema=None) as batch_op:
        batch_op.drop_column('featuring')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song_to_artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('featuring', sa.BOOLEAN(), nullable=False))

    # ### end Alembic commands ###
