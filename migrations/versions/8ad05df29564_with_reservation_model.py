"""With reservation model

Revision ID: 8ad05df29564
Revises: fbf3995d36c6
Create Date: 2021-06-14 02:09:49.763002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ad05df29564'
down_revision = 'fbf3995d36c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('classSession_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classSession_id'], ['class_sessions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservations')
    # ### end Alembic commands ###
