from aiomysql import sa


async def init_mysql(app):
    conf = app['database']
    engine = await sa.create_engine(
        db=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port']
    )
    app['db'] = engine


async def close_mysql(app):
    app['db'].close()
    await app['db'].wait_closed()
