"""added api key data and password to user

Revision ID: 9604033786ee
Revises: daf64f1f355c
Create Date: 2020-10-25 12:21:02.659635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9604033786ee'
down_revision = 'daf64f1f355c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('apiExpiry', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('apiKey', sa.String(), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'apiKey')
    op.drop_column('users', 'apiExpiry')
    # ### end Alembic commands ###
