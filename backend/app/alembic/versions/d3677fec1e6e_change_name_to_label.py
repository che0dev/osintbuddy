"""change name to label

Revision ID: d3677fec1e6e
Revises: fffdefe1a8a5
Create Date: 2023-11-06 01:18:02.235676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3677fec1e6e'
down_revision = 'fffdefe1a8a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('graphs', sa.Column('label', sa.String(), nullable=False))
    op.drop_column('graphs', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('graphs', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('graphs', 'label')
    # ### end Alembic commands ###
