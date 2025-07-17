"""Add email column to users

Revision ID: 1ac9f77afb00
Revises: 9c80307abc46
Create Date: 2025-07-14 23:36:43.391000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ac9f77afb00'
down_revision: Union[str, Sequence[str], None] = '9c80307abc46'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('email', sa.String(), nullable=False, server_default='placeholder@example.com'))


def downgrade() -> None:
    op.drop_column('users', 'email')