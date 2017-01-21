from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
models__question = Table('models__question', post_meta,
    Column('question_id', Integer, primary_key=True, nullable=False),
    Column('content', String(length=2000)),
    Column('user_id', Integer),
    Column('create_date', Integer),
)

models__user = Table('models__user', post_meta,
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
    post_meta.tables['models__question'].columns['create_date'].create()
    post_meta.tables['models__user'].columns['create_date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['models__question'].columns['create_date'].drop()
    post_meta.tables['models__user'].columns['create_date'].drop()
