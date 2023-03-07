"""Add holidays table

Revision ID: 1e981ab7bc29
Revises: 517a33b57a15
Create Date: 2023-03-06 14:26:32.340942

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1e981ab7bc29'
down_revision = '517a33b57a15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('holidays',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('guild_id', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_holidays'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('holidays')
    # ### end Alembic commands ###