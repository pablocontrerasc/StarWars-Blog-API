"""empty message

Revision ID: d760379442ce
Revises: d6ad2ec4dc3f
Create Date: 2022-05-05 05:24:46.477664

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd760379442ce'
down_revision = 'd6ad2ec4dc3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personaje_favoritos', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('personaje_favoritos', 'usuario_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.add_column('planeta_favoritos', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('planeta_favoritos', 'usuario_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('planeta_favoritos', 'usuario_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('planeta_favoritos', 'id')
    op.alter_column('personaje_favoritos', 'usuario_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('personaje_favoritos', 'id')
    # ### end Alembic commands ###
