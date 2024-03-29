"""Add draw_challenges_channel_id column to GuildSettings model

Revision ID: ff8ee392da5c
Revises: 9652f0eda832
Create Date: 2023-08-17 17:41:30.336305

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "ff8ee392da5c"
down_revision = "9652f0eda832"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table("guild_settings", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "draw_challenges_channel_id", sa.String(length=300), nullable=True
            )
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table("guild_settings", schema=None) as batch_op:
        batch_op.drop_column("draw_challenges_channel_id")

    # ### end Alembic commands ###
