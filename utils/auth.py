import python_jwt as jwt
import jwcrypto.jwk as jwk
import datetime
from config.config import JWTConfig
from config import RESP

priv_key = jwk.JWK.from_pem(JWTConfig.priv_pem)
pub_key = jwk.JWK.from_pem(JWTConfig.pub_pem)


def gen_token(user_id, expires=None):
    payload = {"user": user_id}
    if not expires:
        expires = datetime.timedelta(minutes=4)
    token = jwt.generate_jwt(payload, priv_key, 'RS256', expires)
    return token


def parse_token(token):
    try:
        header, claims = jwt.verify_jwt(token, pub_key, ['RS256'])
    except jwt._JWTError:
        # 通常为过期
        return "token expired!"
    except Exception:
        return "token error!"
    else:
        return claims


def login_required(new_fun):
    def call_fun(request, *args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return RESP.token_error(message="token missed!")
        res = parse_token(token)
        if not isinstance(res, dict):
            return RESP.token_error(message=res)
        request.user = res['user']
        return new_fun(request, *args, **kwargs)

    return call_fun


if __name__ == '__main__':
    user_id = '123'
    tok = gen_token(user_id)
    res = parse_token(tok)
    assert res["user"] == user_id
