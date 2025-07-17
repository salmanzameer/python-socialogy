"""Add user_id column to blogs

Revision ID: 0db580a232b0
Revises: 1ac9f77afb00
Create Date: 2025-07-17 03:21:36.905702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0db580a232b0'
down_revision: Union[str, Sequence[str], None] = '1ac9f77afb00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('blogs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'fk_blogs_user_id_users',     # Constraint name
        'blogs',                      # Source table
        'users',                      # Referenced table
        ['user_id'],                  # Local column
        ['id'],                       # Remote column
    )

def downgrade() -> None:
    op.drop_constraint('fk_blogs_user_id_users', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')