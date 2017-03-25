from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
models__answer = Table('models__answer', pre_meta,
    Column('answer_id', INTEGER, primary_key=True, nullable=False),
    Column('content', VARCHAR(length=1024)),
    Column('user_id', INTEGER),
    Column('question_id', INTEGER),
    Column('create_date', INTEGER),
)

models__question = Table('models__question', pre_meta,
    Column('question_id', INTEGER, primary_key=True, nullable=False),
    Column('content', VARCHAR(length=2000)),
    Column('user_id', INTEGER),
    Column('create_date', INTEGER),
)

models__user = Table('models__user', pre_meta,
    Column('user_id', INTEGER, primary_key=True, nullable=False),
    Column('email_address', VARCHAR(length=255)),
    Column('nickname', VARCHAR(length=70)),
    Column('reputation', INTEGER),
    Column('create_date', INTEGER),
)

answer = Table('answer', post_meta,
    Column('answer_id', Integer, primary_key=True, nullable=False),
    Column('content', String(length=1024)),
    Column('user_id', Integer),
    Column('question_id', Integer),
    Column('create_date', Integer),
)

question = Table('question', post_meta,
    Column('question_id', Integer, primary_key=True, nullable=False),
    Column('content', String(length=2000)),
    Column('user_id', Integer),
    Column('create_date', Integer),
)

user = Table('user', post_meta,
    Column('user_id', Integer, primary_key=True, nullable=False),
    Column('email_address', String(length=255)),
    Column('nickname', String(length=70)),
    Column('reputation', Integer),
    Column('create_date', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['models__answer'].drop()
    pre_meta.tables['models__question'].drop()
    pre_meta.tables['models__user'].drop()
    post_meta.tables['answer'].create()
    post_meta.tables['question'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['models__answer'].create()
    pre_meta.tables['models__question'].create()
    pre_meta.tables['models__user'].create()
    post_meta.tables['answer'].drop()
    post_meta.tables['question'].drop()
    post_meta.tables['user'].drop()
