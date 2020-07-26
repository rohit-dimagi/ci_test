"""empty message

Revision ID: 60e4bfeb4874
Revises: 1744cd46c8d2
Create Date: 2020-07-25 23:27:35.491558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60e4bfeb4874'
down_revision = '1744cd46c8d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'person', ['email_address'])
    op.create_unique_constraint(None, 'students', ['student_id'])
    op.create_unique_constraint(None, 'subjects', ['subject_id'])
    op.create_unique_constraint(None, 'teachers', ['staff_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teachers', type_='unique')
    op.drop_constraint(None, 'subjects', type_='unique')
    op.drop_constraint(None, 'students', type_='unique')
    op.drop_constraint(None, 'person', type_='unique')
    # ### end Alembic commands ###