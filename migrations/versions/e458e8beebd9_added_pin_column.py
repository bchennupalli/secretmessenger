"""Added pin column

Revision ID: e458e8beebd9
Revises: 
Create Date: 2024-02-03 19:02:27.573931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e458e8beebd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pin', sa.String(length=8), nullable=False))
        # Specify the name for the unique constraint
        batch_op.create_unique_constraint('uq_message_pin', ['pin'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        # Use the named constraint for dropping it
        batch_op.drop_constraint('uq_message_pin', type_='unique')
        batch_op.drop_column('pin')
    # ### end Alembic commands ###
