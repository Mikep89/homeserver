"""Finalize User table

Revision ID: baa7ac24b56a
Revises: ae6e36bb331e
Create Date: 2020-10-24 20:36:59.435626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baa7ac24b56a'
down_revision = 'ae6e36bb331e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('dateCreated', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    op.drop_column('users', 'dateCreated')
    # ### end Alembic commands ###
