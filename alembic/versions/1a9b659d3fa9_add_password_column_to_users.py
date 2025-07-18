"""Add password column to users

Revision ID: 1a9b659d3fa9
Revises: 0db580a232b0
Create Date: 2025-07-18 03:52:13.294231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a9b659d3fa9'
down_revision: Union[str, Sequence[str], None] = '0db580a232b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('password', sa.String(), nullable=False, server_default='testing123'))


def downgrade() -> None:
    op.drop_column('users', 'password')