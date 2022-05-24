"""empty message

Revision ID: 4f8f50a49cca
Revises: 59d6dc152513
Create Date: 2022-05-23 17:58:57.564406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f8f50a49cca'
down_revision = '59d6dc152513'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('terrain', sa.String(length=120), nullable=False),
    sa.Column('population', sa.String(length=120), nullable=False),
    sa.Column('inhabitants', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
