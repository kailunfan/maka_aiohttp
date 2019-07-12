from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)


meta = MetaData()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('phone', String(40), nullable=True),
    Column('open_id', String(200), nullable=True),
    Column('u_id', String(200), nullable=True),
)

question = Table(
    'question', meta,

    Column('id', Integer, primary_key=True),
    Column('question_text', String(200), nullable=False),
    Column('pub_date', Date, nullable=False)
)

choice = Table(
    'choice', meta,

    Column('id', Integer, primary_key=True),
    Column('choice_text', String(200), nullable=False),
    Column('votes', Integer, server_default="0", nullable=False),
    Column('question_id', Integer, ForeignKey('question.id', ondelete='CASCADE'))
)

