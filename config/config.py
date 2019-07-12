database = {
    "database": "maka",
    "user": "root",
    "password": "123",
    "host": "localhost",
    "port": 3306,
}

server = {
    "host": "127.0.0.1",
    "port": 8080
}


class JWTConfig:
    priv_pem = b'-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC8vCvAXxgYj/gB\nt3lGuI9JYcI1nEl+9Q4+lUjS8tSD7ha0JHcWKrLdgCasSal7BdwX/0W2HNkXSnAV\nthAE84gPS6nj6qE7ayVRZiMxJgVOc6NrGMO6GrWKE+G5hX5OsmoBU43kXuyeZhxq\nf7KvlxFOX2mS/BLSmpV3XPwukLq2H0Mkm1usFj6qz2QVGAV3PKd5Q3AagPmegnWc\npPmwKuBCmPi0nHCau8ZMkswzuepOrIeUhPYBe4Tw0HF0uUGChrJq3DigtKt73F/q\ngLnkIRTn5q6n2QYgLd+2alAvfMnInUO9sTXHvED3wkNfWFxDV8lyTTv886t+D5lX\n7SG/5lk1AgMBAAECggEBALklk3oFD5tQ6IeumE9TUGU5fI6hAcyE0/N6+VTPmMDP\nuQABYb2iJ5N5Wvba0GL6LZ5w8s8jX6gkgu4Zi39/9DKlFEWc74xdoN9IZi+Zz8zV\nTjQKuD+CYiLRPDeGCJFlHu6sK98ja9Y775ZeLUlp1jVfDi9+D20A7q2Iz29S1YdA\nVeXmgQ7SNust8vMFVmaxhuyxjHaihAxlJLCpZUWl4jGnDu9d/kKbFdn77i66n/ID\njU5zmCCa/6Jc8/pq4XkdARRQZIADf5fBq60ZvQkpA0gjXhZLZOuB8/jAmisf4+kl\nwd+c1wimszz5rTsA/AIwORW5lhAxKSoUCRzN9nrdiuECgYEA6Jd5UGoh/P4V47Y0\nQNcupYJQBNdrLGc4PANyhDjeiXqY/7c/6bJ1I84VZR1lXgvlpTbRVAlaaLo8TwuE\nMwP6Ai0W6pg8Ok51QNXn/Yrm8dSyvxeDRSGnH270igzLCWHp4nEZ4pogZ7h9bDrW\n4zITT7M9pjpPvIu64ZK6PH3UeH0CgYEAz7rEk75mMg1akY6ABh6KNmOvwgz6sK6c\nUsfcT5H01FsrctaEsZ9p8LzxWMojMZAMLQfQB32oXsf0jf0ECC7cqwMFHIdPTHqs\npsrUkzpY6UwPzqKHwvtKIwPv0LyFzaIDKUbESTCKX13aq5oTBuz90t+P+mI4zJDj\noZuTZUfZ+RkCgYBogf8hcb651VTyjyDlbYppFadstXpTZkGvPYFMBd1/+lUauTT/\nhY76upOEbnPokQHrfTkLQHSeD+gfQDZzUbsZFTdxy1tse2pV6oclti7UxFRYZnE2\nM8vK5Oj9yofEPHmBpH4UAlrDH/NDGSEKzqo8qnXt5c+EEWi0CGCj44n/ZQKBgQCk\nmz8CRDH/H43RIbZZIwIqrzuq7VYJg5PkFPODKglz7Pq0+UAU8FmmplIpJaRVteuw\nEyzJgs1UreYgTYpQYbIC4VW/kYlI9Tyyvq9MK0QhOmCcQTaLT00kCg6SvZDZrbQL\nlUQdKxW7FEgfCuxg5JMN8pHIuuR/VaDLgth9vT4AoQKBgQCCilndEaagZxfcvrbS\n98MkGTD08+hek6X0RwLpEV1P4GItxkyczGkKWmj8DhXKJeFIyZ78m39/WAipYqL4\nmKPHShp7/mYPd6ee8cSCPyLg/y6wRE0MGPBa8leniIn0eW7KSnnLvv0ZNwWcTqHV\noLUAx0h66kOv9bdrhn1ofX9YbA==\n-----END PRIVATE KEY-----\n'
    pub_pem = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvLwrwF8YGI/4Abd5RriP\nSWHCNZxJfvUOPpVI0vLUg+4WtCR3Fiqy3YAmrEmpewXcF/9FthzZF0pwFbYQBPOI\nD0up4+qhO2slUWYjMSYFTnOjaxjDuhq1ihPhuYV+TrJqAVON5F7snmYcan+yr5cR\nTl9pkvwS0pqVd1z8LpC6th9DJJtbrBY+qs9kFRgFdzyneUNwGoD5noJ1nKT5sCrg\nQpj4tJxwmrvGTJLMM7nqTqyHlIT2AXuE8NBxdLlBgoayatw4oLSre9xf6oC55CEU\n5+aup9kGIC3ftmpQL3zJyJ1DvbE1x7xA98JDX1hcQ1fJck07/POrfg+ZV+0hv+ZZ\nNQIDAQAB\n-----END PUBLIC KEY-----\n'


class ALI:
    aes_key = "s5jrvEma6EQ2FZ0xzzjBeQ=="