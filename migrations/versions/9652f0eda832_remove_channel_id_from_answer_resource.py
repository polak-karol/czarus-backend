"""Remove channel_id from answer resource

Revision ID: 9652f0eda832
Revises: 4bb4b7f17296
Create Date: 2023-08-16 15:03:21.329021

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "9652f0eda832"
down_revision = "4bb4b7f17296"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("answers", schema=None) as batch_op:
        batch_op.drop_column("channel_id")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table("answers", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "channel_id",
                sa.VARCHAR(length=300),
                autoincrement=False,
                nullable=False,
            )
        )

    # ### end Alembic commands ###