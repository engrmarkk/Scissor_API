"""'initial'

Revision ID: 22814c0f7d06
Revises: 
Create Date: 2023-05-10 22:08:43.611531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22814c0f7d06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('links', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('links', schema=None) as batch_op:
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###
