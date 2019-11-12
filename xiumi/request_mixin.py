from json import JSONDecodeError

import requests

from hanfurestful import settings
from xiumi.mixins import XiuMiMixin


class RequestMixin:
    '''
    请求实体 基类
    '''
    url = None
    data = None
    params = None

    def request_init_data(self):
        '''
        初始化请求参数
        :return:
        '''
        return {
            'params': self.get_params(),
            'data': self.get_data()
        }

    def get_data(self):
        '''
        POST 请求参数
        :return:
        '''
        if self.data:
            return self.data
        return {}

    def get_params(self):
        '''
        GET 请求参数
        :return:
        '''
        if self.params:
            return self.params
        return {}

    def request_get(self):
        '''
        GET接口请求
        :return:
        '''
        if not self.url: raise NotImplementedError(
            '{cls}.url must be implemented.'.format(
                cls=self.__class__.__name__
            )
        )

        request_data = self.request_init_data()
        # _re = requests.get(url=self.url, **request_data)
        _re = {}
        try:
            return _re  # .json()
        except JSONDecodeError as e:
            return {
                'code': -100,
                'msg': '请求实体错误：{} | status_code: {} | text: {}'.format(e.args, _re.status_code, _re.text)
            }
        pass

    def request_post(self):
        '''
        POST接口请求
        :return:
        '''
        if not self.url: raise NotImplementedError(
            '{cls}.url must be implemented.'.format(
                cls=self.__class__.__name__
            )
        )
        request_data = self.request_init_data()
        # _re = requests.post(url=self.url, **request_data)
        _re = {}

        try:
            return _re  # .json()
        except JSONDecodeError as e:
            return {
                'code': -100,
                'msg': '请求实体错误：{} | status_code: {} | text: {}'.format(e.args, _re.status_code, _re.text)
            }


class AccessTokenMixin(RequestMixin, XiuMiMixin):
    '''
    获取access_token的接口
    '''
    url = 'http://your-domain.com/some_path_for_access_token?'  # appid={appid}&nonce={nonce}&signature={signature}&timestamp={timestamp}

    def get_params(self):
        c = {
            'appid': self.app_id,
            'nonce': self.get_nonce(),
            'signature': self.get_access_token_signature(),
            'timestamp': self.get_timestamp()
        }

        return c

    pass

class AccessLoginMixin(XiuMiMixin):
    pass


class SomePathArticles(RequestMixin):
    '''
    接收图文内容的接口
    '''
    url = 'http://your-domain.com/some_path_for_articles?'

    def re_get(self):
        _signature = self.get_access_token_signature([
            self.token,
            self.timestamp
        ])
        _signature = self.get_access_token_signature([
            _signature,
            self.uid
        ])
        params = {
            'access_token': self.token,
            'uid': self.uid,
            'signature': _signature,
            'timestamp': self.timestamp
        }
        _re = requests.get(url=self.url, params=params)
        print(_re.status_code)

        try:
            return _re.json()
        except JSONDecodeError as e:
            return {
                'code': -100,
                'msg': '请求实体错误：{} | status_code: {} | text: {}'.format(e.args, _re.status_code, _re.text)
            }
