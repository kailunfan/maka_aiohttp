# encoding: utf-8
from aiohttp.web import json_response


class HttpCode(object):
    param_ok = 0
    token_error = -1
    param_error = 120103
    request_error = 400
    sms_error = 119167
    captcha_error = 102105
    data_not_exist_error = 300001
    condition_error = 300002


def restful_result(code, message, description=""):
    return json_response({"code": code, "message": message, "description": description})


def success(body=None, **kwargs):
    res = {"code": HttpCode.param_ok, "body": body}
    for k in kwargs:
        res[k] = kwargs[k]
    return json_response(res)


def token_error(message="token error"):
    return restful_result(code=HttpCode.token_error, message=message)


def param_error(message="param error"):
    return restful_result(code=HttpCode.param_error, message=message)


def request_error(message="request error"):
    return restful_result(code=HttpCode.request_error, message=message)


def sms_error(message="sms error"):
    return restful_result(code=HttpCode.sms_error, message=message)


def captcha_error(message="sms error"):
    return restful_result(code=HttpCode.captcha_error, message=message)


def data_not_exist_error(message='data not exist'):
    return restful_result(code=HttpCode.data_not_exist_error, message=message)


def condition_error(message="condition error"):
    return restful_result(code=HttpCode.condition_error, message=message)
