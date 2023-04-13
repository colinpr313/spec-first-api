"""new fields in user model

Revision ID: 3847de89ad6a
Revises: 3d7ade9659f6
Create Date: 2023-04-12 21:36:19.540141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3847de89ad6a'
down_revision = '3d7ade9659f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
