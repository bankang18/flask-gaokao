import hashlib
import json
import random
import string
import requests

from application import app


class MemberService:

    @staticmethod
    def geneAuthCode(member_info=None):
        """
        认证码
        :param member_info: 用户对象
        :return: 加密后的cookie
        """
        m = hashlib.md5()
        str = "%s-%s-%s" % (member_info.id, member_info.salt, member_info.status)
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))

    @staticmethod
    def getWeChatOpenId(code):
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}' \
              '&secret={1}&js_code={2}&grant_type=authorization_code' \
            .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
        r = requests.get(url, verify=False)
        # app.logger.debug(json.loads(r.text))
        res = json.loads(r.text)
        openid = None
        if 'openid' in res:
            openid = res['openid']

        return openid
