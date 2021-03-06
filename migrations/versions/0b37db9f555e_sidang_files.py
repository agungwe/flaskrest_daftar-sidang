"""sidang files

Revision ID: 0b37db9f555e
Revises: cf412a5f69fc
Create Date: 2020-09-18 16:12:05.502409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b37db9f555e'
down_revision = 'cf412a5f69fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sidang_files',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('sidang_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['sidang_id'], ['sidangs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sidang_files_created_at'), 'sidang_files', ['created_at'], unique=False)
    op.create_index(op.f('ix_sidang_files_updated_at'), 'sidang_files', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sidang_files_updated_at'), table_name='sidang_files')
    op.drop_index(op.f('ix_sidang_files_created_at'), table_name='sidang_files')
    op.drop_table('sidang_files')
    # ### end Alembic commands ###
