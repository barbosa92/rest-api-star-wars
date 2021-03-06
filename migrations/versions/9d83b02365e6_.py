"""empty message

Revision ID: 9d83b02365e6
Revises: 0bb786d88658
Create Date: 2022-06-05 18:12:19.369732

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9d83b02365e6'
down_revision = '0bb786d88658'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.drop_index('email', table_name='user')
    op.drop_index('email_2', table_name='user')
    op.drop_table('user')
    op.drop_constraint('fav_people_ibfk_2', 'fav_people', type_='foreignkey')
    op.create_foreign_key(None, 'fav_people', 'users', ['user_id'], ['id'])
    op.drop_constraint('fav_planet_ibfk_2', 'fav_planet', type_='foreignkey')
    op.create_foreign_key(None, 'fav_planet', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fav_planet', type_='foreignkey')
    op.create_foreign_key('fav_planet_ibfk_2', 'fav_planet', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'fav_people', type_='foreignkey')
    op.create_foreign_key('fav_people_ibfk_2', 'fav_people', 'user', ['user_id'], ['id'])
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`is_active` in (0,1))', name='user_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('email_2', 'user', ['email'], unique=False)
    op.create_index('email', 'user', ['email'], unique=False)
    op.drop_table('users')
    # ### end Alembic commands ###
