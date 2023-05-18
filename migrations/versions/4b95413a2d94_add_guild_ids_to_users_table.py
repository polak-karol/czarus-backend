"""Add guild_ids to users table

Revision ID: 4b95413a2d94
Revises: 1111dbbdee82
Create Date: 2023-05-18 11:43:05.696746

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4b95413a2d94'
down_revision = '1111dbbdee82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('guild_ids', postgresql.ARRAY(sa.String()), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('guild_ids')

    # ### end Alembic commands ###