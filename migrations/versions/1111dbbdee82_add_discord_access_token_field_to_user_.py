"""Add discord_access_token field to user model

Revision ID: 1111dbbdee82
Revises: 30f50c56d57c
Create Date: 2023-05-11 14:47:20.734505

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "1111dbbdee82"
down_revision = "30f50c56d57c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("discord_access_token", sa.String(length=128), nullable=True)
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("discord_access_token")

    # ### end Alembic commands ###