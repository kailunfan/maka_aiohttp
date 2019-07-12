from aiohttp.web import json_response
from aiomysql import Connection
from aiomysql.sa import SAConnection, Engine

from db import model
from utils.auth import login_required
from config import RESP
from utils.auth import gen_token


async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(model.user.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]
        return json_response(questions)


async def login(request):
    """通过手机号登录"""
    data = await request.post()
    if not data or not data.get("phone"):
        return RESP.param_error("phone missed!")
    async with request.app['db'].acquire() as conn:
        phone = data.get('phone')
        cursor = await conn.execute(model.user.select(f"phone={phone}"))
        user = await cursor.first()
        if user:
            user_id = user.id
        else:
            # 手机号不存在则注册
            if not user:
                conn: SAConnection = conn
                await conn.execute(model.user.insert().values(phone=phone))
                user_id = conn.connection.insert_id()
                await conn.connection.commit()

        token = gen_token(user_id)
        return RESP.success(body={"id": user_id}, token=token)


# async def login(request):
#     """通过手机号登录"""
#     data = await request.post()
#     if not data or not data.get("phone"):
#         return RESP.param_error("phone missed!")
#     for i in range(10):
#         conn = await request.app['db'].acquire()
#         phone = data.get('phone')
#         cursor = await conn.execute(model.user.select(f"phone={phone}"))
#         user = await cursor.first()
#         # await conn.close()
#
#     return RESP.success(body={"id": user.id}, token="ttt")


@login_required
async def user(request):
    """
    获取用户详情
    :param request:
    :return:
    """
    id = request.user
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(model.user.select(f"id={id}"))
        records = await cursor.first()
        return json_response(dict(records))
