"""empty message

Revision ID: d6ad2ec4dc3f
Revises: 15791a4b1d49
Create Date: 2022-05-05 02:42:04.947322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6ad2ec4dc3f'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('height', sa.String(length=100), nullable=True),
    sa.Column('mass', sa.String(length=100), nullable=True),
    sa.Column('hair_color', sa.String(length=100), nullable=True),
    sa.Column('skin_color', sa.String(length=100), nullable=True),
    sa.Column('eye_color', sa.String(length=100), nullable=True),
    sa.Column('birth_year', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=100), nullable=True),
    sa.Column('homeworld', sa.String(length=150), nullable=True),
    sa.Column('created', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('orbital_period', sa.String(length=100), nullable=True),
    sa.Column('rotation_period', sa.String(length=100), nullable=True),
    sa.Column('diameter', sa.String(length=100), nullable=True),
    sa.Column('climate', sa.String(length=100), nullable=True),
    sa.Column('gravity', sa.String(length=100), nullable=True),
    sa.Column('terrain', sa.String(length=100), nullable=True),
    sa.Column('surface_water', sa.String(length=100), nullable=True),
    sa.Column('population', sa.String(length=100), nullable=True),
    sa.Column('created', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('apellido', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('fecha_subscripcion', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personaje_favoritos',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('personaje_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('usuario_id')
    )
    op.create_table('planeta_favoritos',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('planeta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('usuario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planeta_favoritos')
    op.drop_table('personaje_favoritos')
    op.drop_table('usuario')
    op.drop_table('planeta')
    op.drop_table('personaje')
    # ### end Alembic commands ###