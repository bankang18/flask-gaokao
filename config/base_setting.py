SERVER_PORT = 8999
DEBUG = False
JSON_AS_ASCII = False
SQLALCHEY_ECHO = False

# cookie认证管理员是否已登陆 key
AUTH_COOKIE_NAME = 'gaokao-guanliyuan'

# 过滤url认证拦截
IGNORE_URLS = [
    "^/user/login",
    "/api"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico",
    "^/api"
]

# 域名
APP = {
    'domain': 'http://10.1.44.246:8999/'
}

UPLOAD = {
    'ext': ['jpg', 'png', 'gif', 'jpeg','bmp'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}