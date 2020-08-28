"""empty message

Revision ID: 563175164329
Revises: d13346a6c40e
Create Date: 2020-08-28 03:55:38.578474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '563175164329'
down_revision = 'd13346a6c40e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_mail', sa.String(length=40), nullable=True))
    op.add_column('user', sa.Column('user_role', sa.String(length=10), nullable=True))
    op.drop_column('user', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('user', 'user_role')
    op.drop_column('user', 'user_mail')
    # ### end Alembic commands ###
