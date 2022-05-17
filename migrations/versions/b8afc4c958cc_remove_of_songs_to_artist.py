"""remove # of songs to artist

Revision ID: b8afc4c958cc
Revises: feee4f25dd19
Create Date: 2022-05-16 21:13:34.807858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8afc4c958cc'
down_revision = 'feee4f25dd19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.drop_column('number_of_songs')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number_of_songs', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###