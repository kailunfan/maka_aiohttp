from sqlalchemy import create_engine, MetaData
from db.model import question, choice, user
from config.config import database
import pymysql

pymysql.install_as_MySQLdb()

ADMIN_DB_URL = "mysql://{user}:{password}@{host}:{port}/{database}".format_map(database)
admin_engine = create_engine(ADMIN_DB_URL, isolation_level='AUTOCOMMIT')


def create_tables(engine=admin_engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice, user])


def drop_tables(engine=admin_engine):
    meta = MetaData()
    meta.drop_all(bind=engine, tables=[question, choice])


if __name__ == '__main__':
    print(ADMIN_DB_URL)
    pass
    # create_tables(engine=admin_engine)
