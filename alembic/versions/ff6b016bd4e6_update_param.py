"""update param

Revision ID: ff6b016bd4e6
Revises: 223d5b6850f0
Create Date: 2024-06-08 17:17:28.776646

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff6b016bd4e6'
down_revision: Union[str, None] = '223d5b6850f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('target_market', sa.String(), nullable=True))
    op.add_column('companies', sa.Column('technology', sa.String(), nullable=True))
    op.add_column('companies', sa.Column('revenue_stream', sa.String(), nullable=True))
    op.create_index(op.f('ix_companies_revenue_stream'), 'companies', ['revenue_stream'], unique=False)
    op.create_index(op.f('ix_companies_target_market'), 'companies', ['target_market'], unique=False)
    op.create_index(op.f('ix_companies_technology'), 'companies', ['technology'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_companies_technology'), table_name='companies')
    op.drop_index(op.f('ix_companies_target_market'), table_name='companies')
    op.drop_index(op.f('ix_companies_revenue_stream'), table_name='companies')
    op.drop_column('companies', 'revenue_stream')
    op.drop_column('companies', 'technology')
    op.drop_column('companies', 'target_market')
    # ### end Alembic commands ###