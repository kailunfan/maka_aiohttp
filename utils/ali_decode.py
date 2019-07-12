#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.config import ALI
from alipay.aop.api.util import EncryptUtils

resp = {
    "response": "dmwZpI3E7h1+FuplMR52k3DfR4mOT0EyxU3gG7xYshy5MZRiD+1F8jAFhItufNzzjZIyg8j7KFDquRuWNSsx6Ijni9iVj01H/fxV+fFXS4jkTXdFgAiXuyoYDiDRen27RlaewMpCGpKQEbj3eIzGA2LdKO0clMNTxFWyexcfoUxONgoBlxIrEFINxGk/QAL5wrNinnXVWWdiCUed31IzHGiYvCwo12LgeXUDlyJh6OZQQXh1ejBsdG29qcLyA1cl",
    "sign": "ruKKABt8KK1gNu36BvFCKcoeSqe5dZ4zqMWSF8HILsLWs3JGl2ES/xXxykLQ4xE+YBe08Ji0Pza9Eoc/YQ+ntDerW4guAjg+Pqn7/BcssM2W3Of67HYgAHjPtYzhf9rHAjfGPv48BZpcpNs4/TDt46S5csZlMtTPRa40nOR/V5Drb3DLdkH2LrD2+7yYsxGw8ZcBxcBYmO5uZofSUg9fiyWTZ5eYm9QveBu23BH2aHhlNIJv7q0iQ12TKPPksw6FgJV0FK0FrsktaGqFIQIhPBqS0hC5kDXwdKIJZeGFpsAKCIOgT8ztfsXpISbyKprLg+3/Eri3f31Ul4AkTenE0Q=="
}


def decrypt_phone(response):
    return EncryptUtils.decrypt_content(response, "AES", "hLX5KjHFc/7JkUZy24Gz2w==", "UTF-8")


if __name__ == '__main__':
    # res = EncryptUtils.decrypt_content(resp["response"], "AES", ALI.aes_key, 'utf-8')
    # print(res)

    b = EncryptUtils.encrypt_content("Hello,world!!!", "AES", "hLX5KjHFc/7JkUZy24Gz2w==", "UTF-8")
    print(b)

    a = decrypt_phone("OIL6ZOXZLFdB41ZMlylvHXdiE6R9HX6qG6W7y0fBWl1S90nPap5/mz0o2A35uLMw9PJQnIu/gg+2mcp9rmtM7Q==")
    print(a)
