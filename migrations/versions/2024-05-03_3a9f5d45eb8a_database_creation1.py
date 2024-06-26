"""Database creation1

Revision ID: 3a9f5d45eb8a
Revises: 
Create Date: 2024-05-03 19:51:05.199032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3a9f5d45eb8a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('city', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('education',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('education', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('employment_type',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('employment_type', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('programming_language',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('programming_language', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('specialization',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('specialization', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('work_experience',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('work_experience', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('work_location',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('work_location', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('work_schedule',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('work_schedule', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('favorite_filters',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user', sa.Integer(), nullable=True),
                    sa.Column('salary_range_min', sa.Numeric(), nullable=True),
                    sa.Column('salary_range_max', sa.Numeric(), nullable=True),
                    sa.Column('city', sa.Integer(), nullable=True),
                    sa.Column('work_location', sa.Integer(), nullable=True),
                    sa.Column('employment_type', sa.Integer(), nullable=True),
                    sa.Column('specialization', sa.Integer(), nullable=True),
                    sa.Column('education', sa.Integer(), nullable=True),
                    sa.Column('work_experience', sa.Integer(), nullable=True),
                    sa.Column('work_schedule', sa.Integer(), nullable=True),
                    sa.Column('programming_language', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['city'], ['city.id'], ),
                    sa.ForeignKeyConstraint(['education'], ['education.id'], ),
                    sa.ForeignKeyConstraint(['employment_type'], ['employment_type.id'], ),
                    sa.ForeignKeyConstraint(['programming_language'], ['programming_language.id'], ),
                    sa.ForeignKeyConstraint(['specialization'], ['specialization.id'], ),
                    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['work_experience'], ['work_experience.id'], ),
                    sa.ForeignKeyConstraint(['work_location'], ['work_location.id'], ),
                    sa.ForeignKeyConstraint(['work_schedule'], ['work_schedule.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('vacancy',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('salary_range_min', sa.Numeric(), nullable=True),
                    sa.Column('salary_range_max', sa.Numeric(), nullable=True),
                    sa.Column('city', sa.Integer(), nullable=True),
                    sa.Column('work_location', sa.Integer(), nullable=True),
                    sa.Column('employment_type', sa.Integer(), nullable=True),
                    sa.Column('specialization', sa.Integer(), nullable=True),
                    sa.Column('education', sa.Integer(), nullable=True),
                    sa.Column('work_experience', sa.Integer(), nullable=True),
                    sa.Column('work_schedule', sa.Integer(), nullable=True),
                    sa.Column('programming_language', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['city'], ['city.id'], ),
                    sa.ForeignKeyConstraint(['education'], ['education.id'], ),
                    sa.ForeignKeyConstraint(['employment_type'], ['employment_type.id'], ),
                    sa.ForeignKeyConstraint(['programming_language'], ['programming_language.id'], ),
                    sa.ForeignKeyConstraint(['specialization'], ['specialization.id'], ),
                    sa.ForeignKeyConstraint(['work_experience'], ['work_experience.id'], ),
                    sa.ForeignKeyConstraint(['work_location'], ['work_location.id'], ),
                    sa.ForeignKeyConstraint(['work_schedule'], ['work_schedule.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('favorite_vacancy',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user', sa.Integer(), nullable=True),
                    sa.Column('vacancy', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['vacancy'], ['vacancy.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_vacancy')
    op.drop_table('vacancy')
    op.drop_table('favorite_filters')
    op.drop_table('work_schedule')
    op.drop_table('work_location')
    op.drop_table('work_experience')
    op.drop_table('user')
    op.drop_table('specialization')
    op.drop_table('programming_language')
    op.drop_table('employment_type')
    op.drop_table('education')
    op.drop_table('city')
    # ### end Alembic commands ###
