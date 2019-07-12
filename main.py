from aiohttp import web
from db.init import close_mysql, init_mysql
from middlewares import setup_middlewares
from routes import setup_routes

from config.config import database, server
from config import log


async def init_app():
    app = web.Application()
    app['database'] = database

    # create db connection on startup, shutdown on exit
    app.on_startup.append(init_mysql)
    app.on_cleanup.append(close_mysql)

    # setup views and routes
    setup_routes(app)

    setup_middlewares(app)

    return app


if __name__ == '__main__':
    log.set_log()
    app = init_app()
    web.run_app(app, host=server['host'], port=server['port'])
