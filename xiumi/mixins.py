import random


class XiuMiMixin(object):
    uid = '21312423'
    app_id = '2edwdqwda'
    token = 'adasdasda'
    secret = 'qwdasdadad'
    timestamp = '234123123'
    nonce = None

    def _signature(self, signature):
        '''
        signature签名算法
        :param signature:
        :return:
        '''
        import hashlib

        signature_str = ''.join(signature).encode('utf-8')
        md = hashlib.md5()
        md.update(signature_str)
        return md.hexdigest()

    def _ran(self, index):
        '''
        生成随机字符串
        :param index:
        :return:
        '''
        _str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        _salt = ''

        for i in range(index):
            _salt += random.choice(_str)

        return _salt

    def get_nonce(self):
        '''
        返回 生成随机字符串
        :return:
        '''
        self.nonce = self._ran(6)
        return self.nonce

    def get_access_token_signature(self):
        '''
        access_token的接口 signature签名算法
        :return:
        '''
        signature = [self.secret, self.timestamp, self.nonce, self.app_id]
        print('signature', signature)
        signature.sort()
        return self._signature(signature)

    pass
