"""create_polls_table

Revision ID: 13ad2e97fb43
Revises: e9e939b54077
Create Date: 2024-09-24 15:27:55.602950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import enum


class PollType(enum.Enum):
    text = 1
    image = 2
    three = 3

# revision identifiers, used by Alembic.
revision: str = '13ad2e97fb43'
down_revision: Union[str, None] = 'e9e939b54077'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('type', sa.Enum(PollType), nullable=False),
        sa.Column('is_add_choices_active', sa.Boolean, nullable=False),
        sa.Column('is_voting_active', sa.Boolean(100), nullable=False),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('polls')
