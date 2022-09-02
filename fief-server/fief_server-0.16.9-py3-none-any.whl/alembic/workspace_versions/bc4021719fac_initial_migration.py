"""Initial migration

Revision ID: bc4021719fac
Revises:
Create Date: 2022-04-13 15:36:14.370753

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

import fief

# revision identifiers, used by Alembic.
revision = "bc4021719fac"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    connection = op.get_bind()
    if connection.dialect.name == "postgresql":
        client_type_enum = postgresql.ENUM(
            "public", "confidential", name="clienttype", create_type=False
        )
        client_type_enum.create(connection, checkfirst=True)
    else:
        client_type_enum = sa.Enum("public", "confidential", name="clienttype")

    op.create_table(
        "fief_tenants",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("default", sa.Boolean(), nullable=False),
        sa.Column("sign_jwk", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index(
        op.f("ix_fief_tenants_created_at"), "fief_tenants", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_fief_tenants_updated_at"), "fief_tenants", ["updated_at"], unique=False
    )
    op.create_table(
        "fief_clients",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("first_party", sa.Boolean(), nullable=False),
        sa.Column(
            "client_type",
            client_type_enum,
            server_default="confidential",
            nullable=False,
        ),
        sa.Column("client_id", sa.String(length=255), nullable=False),
        sa.Column("client_secret", sa.String(length=255), nullable=False),
        sa.Column("redirect_uris", sa.JSON(), nullable=False),
        sa.Column("encrypt_jwk", sa.Text(), nullable=True),
        sa.Column("tenant_id", fief.models.generics.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["tenant_id"], ["fief_tenants.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_fief_clients_client_id"), "fief_clients", ["client_id"], unique=False
    )
    op.create_index(
        op.f("ix_fief_clients_client_secret"),
        "fief_clients",
        ["client_secret"],
        unique=False,
    )
    op.create_index(
        op.f("ix_fief_clients_created_at"), "fief_clients", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_fief_clients_updated_at"), "fief_clients", ["updated_at"], unique=False
    )
    op.create_table(
        "fief_users",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("tenant_id", fief.models.generics.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["tenant_id"], ["fief_tenants.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email", "tenant_id"),
    )
    op.create_index(
        op.f("ix_fief_users_created_at"), "fief_users", ["created_at"], unique=False
    )
    op.create_index(op.f("ix_fief_users_email"), "fief_users", ["email"], unique=False)
    op.create_index(
        op.f("ix_fief_users_updated_at"), "fief_users", ["updated_at"], unique=False
    )
    op.create_table(
        "fief_authorization_codes",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("code", sa.String(length=255), nullable=False),
        sa.Column("c_hash", sa.String(length=255), nullable=False),
        sa.Column("redirect_uri", sa.String(length=2048), nullable=False),
        sa.Column("scope", sa.JSON(), nullable=False),
        sa.Column(
            "authenticated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.Column("nonce", sa.String(length=255), nullable=True),
        sa.Column("code_challenge", sa.String(length=255), nullable=True),
        sa.Column("code_challenge_method", sa.String(length=255), nullable=True),
        sa.Column("user_id", fief.models.generics.GUID(), nullable=False),
        sa.Column("client_id", fief.models.generics.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["client_id"], ["fief_clients.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["fief_users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_fief_authorization_codes_code"),
        "fief_authorization_codes",
        ["code"],
        unique=True,
    )
    op.create_index(
        op.f("ix_fief_authorization_codes_created_at"),
        "fief_authorization_codes",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_fief_authorization_codes_updated_at"),
        "fief_authorization_codes",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "fief_grants",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("scope", sa.JSON(), nullable=False),
        sa.Column("user_id", fief.models.generics.GUID(), nullable=False),
        sa.Column("client_id", fief.models.generics.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["client_id"], ["fief_clients.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["fief_users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "client_id"),
    )
    op.create_index(
        op.f("ix_fief_grants_created_at"), "fief_grants", ["created_at"], unique=False
    )
    op.create_index(
        op.f("ix_fief_grants_updated_at"), "fief_grants", ["updated_at"], unique=False
    )
    op.create_table(
        "fief_login_sessions",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("token", sa.String(length=255), nullable=False),
        sa.Column("response_type", sa.String(length=255), nullable=False),
        sa.Column("response_mode", sa.String(length=255), nullable=False),
        sa.Column("redirect_uri", sa.String(length=2048), nullable=False),
        sa.Column("scope", sa.JSON(), nullable=False),
        sa.Column("prompt", sa.String(length=255), nullable=True),
        sa.Column("state", sa.String(length=2048), nullable=True),
        sa.Column("nonce", sa.String(length=255), nullable=True),
        sa.Column("code_challenge", sa.String(length=255), nullable=True),
        sa.Column("code_challenge_method", sa.String(length=255), nullable=True),
        sa.Column("client_id", fief.models.generics.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["client_id"], ["fief_clients.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_fief_login_sessions_created_at"),
        "fief_login_sessions",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_fief_login_sessions_token"),
        "fief_login_sessions",
        ["token"],
        unique=True,
    )
    op.create_index(
        op.f("ix_fief_login_sessions_updated_at"),
        "fief_login_sessions",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "fief_refresh_tokens",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("token", sa.String(length=255), nullable=False),
        sa.Column(
            "expires_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.Column("scope", sa.JSON(), nullable=False),
        sa.Column(
            "authenticated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.Column("user_id", fief.models.generics.GUID(), nullable=False),
        sa.Column("client_id", fief.models.generics.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["client_id"], ["fief_clients.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["fief_users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_fief_refresh_tokens_created_at"),
        "fief_refresh_tokens",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_fief_refresh_tokens_expires_at"),
        "fief_refresh_tokens",
        ["expires_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_fief_refresh_tokens_token"),
        "fief_refresh_tokens",
        ["token"],
        unique=True,
    )
    op.create_index(
        op.f("ix_fief_refresh_tokens_updated_at"),
        "fief_refresh_tokens",
        ["updated_at"],
        unique=False,
    )
    op.create_table(
        "fief_session_tokens",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("token", sa.String(length=255), nullable=False),
        sa.Column(
            "expires_at",
            fief.models.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.Column("user_id", fief.models.generics.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["fief_users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_fief_session_tokens_created_at"),
        "fief_session_tokens",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_fief_session_tokens_expires_at"),
        "fief_session_tokens",
        ["expires_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_fief_session_tokens_token"),
        "fief_session_tokens",
        ["token"],
        unique=True,
    )
    op.create_index(
        op.f("ix_fief_session_tokens_updated_at"),
        "fief_session_tokens",
        ["updated_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_fief_session_tokens_updated_at"), table_name="fief_session_tokens"
    )
    op.drop_index(
        op.f("ix_fief_session_tokens_token"), table_name="fief_session_tokens"
    )
    op.drop_index(
        op.f("ix_fief_session_tokens_expires_at"), table_name="fief_session_tokens"
    )
    op.drop_index(
        op.f("ix_fief_session_tokens_created_at"), table_name="fief_session_tokens"
    )
    op.drop_table("fief_session_tokens")
    op.drop_index(
        op.f("ix_fief_refresh_tokens_updated_at"), table_name="fief_refresh_tokens"
    )
    op.drop_index(
        op.f("ix_fief_refresh_tokens_token"), table_name="fief_refresh_tokens"
    )
    op.drop_index(
        op.f("ix_fief_refresh_tokens_expires_at"), table_name="fief_refresh_tokens"
    )
    op.drop_index(
        op.f("ix_fief_refresh_tokens_created_at"), table_name="fief_refresh_tokens"
    )
    op.drop_table("fief_refresh_tokens")
    op.drop_index(
        op.f("ix_fief_login_sessions_updated_at"), table_name="fief_login_sessions"
    )
    op.drop_index(
        op.f("ix_fief_login_sessions_token"), table_name="fief_login_sessions"
    )
    op.drop_index(
        op.f("ix_fief_login_sessions_created_at"), table_name="fief_login_sessions"
    )
    op.drop_table("fief_login_sessions")
    op.drop_index(op.f("ix_fief_grants_updated_at"), table_name="fief_grants")
    op.drop_index(op.f("ix_fief_grants_created_at"), table_name="fief_grants")
    op.drop_table("fief_grants")
    op.drop_index(
        op.f("ix_fief_authorization_codes_updated_at"),
        table_name="fief_authorization_codes",
    )
    op.drop_index(
        op.f("ix_fief_authorization_codes_created_at"),
        table_name="fief_authorization_codes",
    )
    op.drop_index(
        op.f("ix_fief_authorization_codes_code"), table_name="fief_authorization_codes"
    )
    op.drop_table("fief_authorization_codes")
    op.drop_index(op.f("ix_fief_users_updated_at"), table_name="fief_users")
    op.drop_index(op.f("ix_fief_users_email"), table_name="fief_users")
    op.drop_index(op.f("ix_fief_users_created_at"), table_name="fief_users")
    op.drop_table("fief_users")
    op.drop_index(op.f("ix_fief_clients_updated_at"), table_name="fief_clients")
    op.drop_index(op.f("ix_fief_clients_created_at"), table_name="fief_clients")
    op.drop_index(op.f("ix_fief_clients_client_secret"), table_name="fief_clients")
    op.drop_index(op.f("ix_fief_clients_client_id"), table_name="fief_clients")
    op.drop_table("fief_clients")
    op.drop_index(op.f("ix_fief_tenants_updated_at"), table_name="fief_tenants")
    op.drop_index(op.f("ix_fief_tenants_created_at"), table_name="fief_tenants")
    op.drop_table("fief_tenants")

    try:
        client_type_enum = postgresql.ENUM(
            "public", "confidential", name="clienttype", create_type=False
        )
        client_type_enum.drop(op.get_bind(), checkfirst=True)
    except AttributeError:
        pass
    # ### end Alembic commands ###
