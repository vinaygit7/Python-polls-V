"""create_user_table

Revision ID: e9e939b54077
Revises: 
Create Date: 2024-09-23 16:33:56.817175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9e939b54077'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
