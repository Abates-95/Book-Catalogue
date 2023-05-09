"""empty message

Revision ID: f54bf4224f09
Revises: 
Create Date: 2023-05-08 13:12:33.018918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f54bf4224f09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('book',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('year_published', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('genre', sa.String(length=150), nullable=False),
    sa.Column('author', sa.String(length=150), nullable=False),
    sa.Column('ISBN', sa.String(length=100), nullable=False),
    sa.Column('page_count', sa.String(length=20), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('book_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['book_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    op.drop_table('user')
    # ### end Alembic commands ###
