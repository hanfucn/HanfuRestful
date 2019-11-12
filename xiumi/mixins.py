import hashlib
import random

from django.utils import datetime_safe

from hanfurestful import settings


class XiuMiMixin:
    '''
    米秀签名算法
    '''
    uid = '100035667161'
    app_id = settings.APP_ID
    token = settings.TOKEN
    secret = settings.SECRET
    timestamp = None
    nonce = None

    def us_init(self):
        '''
        初始化签名算法
        :return:
        '''
        self.set_timestamp()
        self.set_nonce()

    def us_signature(self, signature):
        '''
        signature签名算法
        :param signature:
        :return:
        '''

        signature_str = ''.join(signature).encode('utf-8')
        md = hashlib.md5()
        md.update(signature_str)
        return md.hexdigest()

    def set_timestamp(self):
        '''
        设置时间戳
        :return:
        '''
        self.timestamp = int(datetime_safe.datetime.timestamp(datetime_safe.datetime.now()))
        return self.get_timestamp()

    def set_nonce(self):
        '''
        生成随机字符串
        :return:
        '''

        def set_ran(index):
            '''
            生成随机字符串
            :param index:
            :return:
            '''
            _str = 'abcdefghijklmnopqrstuvwxyz0123456789'
            _salt = ''

            for i in range(index):
                _salt += random.choice(_str)

            return _salt

        self.nonce = set_ran(6)
        return self.nonce

    def get_timestamp(self):
        return self.timestamp

    def get_nonce(self):
        '''
        返回随机字符串
        :return:
        '''
        return self.nonce

    def set_signature(self, signature=None):
        self.us_init()

        signature = [str(self.token), str(self.timestamp), str(self.nonce), str(self.uid)]

        signature.sort()
        print('sort', signature)
        _sx = ''.join(signature)  # .lower()
        print('new ', _sx)

        return self.us_signature(_sx)

    def get_access_token_signature(self, signature=None):
        '''
        秀米提供的接口
        access_token的接口 signature 签名算法
        :return:
        '''
        if not signature is None and not type(signature) is list: raise NotImplementedError(
            '{cls}.signature 类型为list.'.format(
                cls=self.__class__.__name__
            )
        )

        return self.set_signature()

    pass

    def get_authentication_login_uri(self):

        cc = 'http://xiumi.us/auth/partner/login?route_type=article&uid={uid}&appid={appid}&nonce={nonce}&signature={signature}&timestamp={timestamp}&mediaid=0'.format(
            uid=self.uid,
            appid=self.app_id,
            nonce=self.nonce,
            signature=ss,
            timestamp=self.timestamp
        )

        print('cc', cc)
        return cc
