"""add-batch-session

Revision ID: c092dabf3ee5
Revises: c1409ad0e8da
Create Date: 2019-08-01 15:18:20.306290

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "c092dabf3ee5"
down_revision = "48ab2dfefba9"
branch_labels = None
depends_on = None


sessiontypes = postgresql.ENUM("INTERACTIVE", "BATCH", name="sessiontypes")


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("kernels", sa.Column("startup_command", sa.Text(), nullable=True))
    op.drop_column("kernels", "type")
    op.add_column(
        "kernels",
        sa.Column(
            "sess_type",
            sa.Enum("INTERACTIVE", "BATCH", name="sessiontypes"),
            nullable=False,
            server_default="INTERACTIVE",
        ),
    )
    op.create_index(op.f("ix_kernels_sess_type"), "kernels", ["sess_type"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_kernels_sess_type"), table_name="kernels")
    op.drop_column("kernels", "sess_type")
    op.add_column(
        "kernels",
        sa.Column(
            "type",
            sa.Enum("INTERACTIVE", "BATCH", name="sessiontypes"),
            nullable=False,
            server_default="INTERACTIVE",
        ),
    )
    op.drop_column("kernels", "startup_command")
    # ### end Alembic commands ###
