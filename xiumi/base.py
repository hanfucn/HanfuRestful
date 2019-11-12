import hashlib
import random

from django.utils import datetime_safe
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSetMixin

from hanfurestful import settings


class GenericXiuMiAPIBase(ViewSetMixin, GenericAPIView):

    def __init__(self, **kwargs):
        self.uid = '100035667161'
        self.app_id = settings.APP_ID
        self.token = settings.TOKEN
        self.secret = settings.SECRET
        self.timestamp = self.set_timestamp()
        self.nonce = self.set_nonce()
        super(GenericXiuMiAPIBase, self).__init__(**kwargs)

    def set_timestamp(self):
        '''
        设置时间戳
        :return:
        '''
        return int(datetime_safe.datetime.timestamp(datetime_safe.datetime.now()))

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

        return set_ran(6)

    def get_timestamp(self):
        return self.timestamp

    def get_nonce(self):
        return self.nonce

    def set_signature(self, signature=None):
        '''

        :param signature:
        :return:
        '''

        def us_signature(_signature):
            '''
            signature签名算法
            :param signature:
            :return:
            '''

            signature_str = ''.join(_signature).encode('utf-8')
            md = hashlib.md5()
            md.update(signature_str)
            return md.hexdigest()

        if not signature:
            signature = [str(self.token), str(self.timestamp), str(self.nonce), str(self.uid)]
            signature.sort()

        return us_signature(signature)

    def get_access_token_signature(self, signature=None):
        '''
        秀米提供的接口
        access_token的接口 signature 签名算法
        :return:
        '''
        return self.set_signature()

    def get_authentication_login_uri(self):
        '''
        用户登录入口
        :return:
        '''
        signature = self.set_signature(self.set_signature())
        login_uri = 'https://xiumi.us/auth/partner/login?route_type=article&uid={uid}&appid={appid}&nonce={nonce}&signature={signature}&timestamp={timestamp}&mediaid=0'.format(
            uid=self.uid,
            appid=self.app_id,
            nonce=self.nonce,
            signature=signature,
            timestamp=self.timestamp
        )

        print('login_uri', login_uri)
        return login_uri

    def set_authentication_token_create(self):
        '''
        生成token
        :return:
        '''
        return 'eex2ohB7thoh3veezishaezi'
