"""create_notepad_model

Revision ID: 2b2dcddf204b
Revises: 001
Create Date: 2024-12-28 13:49:12.689919

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2b2dcddf204b'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notepad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('follow')
    op.drop_table('social')
    op.drop_table('ratings')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ratings',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('dataset_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('quality', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('size', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('usability', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('total_rating', mysql.FLOAT(), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['data_set.id'], name='ratings_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='ratings_ibfk_2', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('social',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('text', mysql.VARCHAR(length=256), nullable=False),
    sa.Column('comment', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('follower', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('followed', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('data_set', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['data_set'], ['data_set.id'], name='social_ibfk_1'),
    sa.ForeignKeyConstraint(['followed'], ['user.id'], name='social_ibfk_2'),
    sa.ForeignKeyConstraint(['follower'], ['user.id'], name='social_ibfk_3'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('follow',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('follower_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('followed_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], name='follow_ibfk_1'),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name='follow_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('notepad')
    # ### end Alembic commands ###