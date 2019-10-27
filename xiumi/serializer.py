from rest_framework import serializers

from xiumi import models


class AccessTokenSerializer(serializers.ModelSerializer):

    def get_signature(self):
        '''
        signature签名算法
        将 secret，timestamp，nonce，appid 四个参数的值以字符串形式由低到高排序，
        然后将四个字符串依次连接为一个字符串，然后用md5函数计算两次哈希，
        得到signature字符串。其中secret由秀米提前颁发，形式为一个32个字符的字符串。
        :return:
        '''

        secret = ''

        signature = [self.timestamp, self.nonce, self.appid, secret]
        signature.sort()
        signature_str = ''.join(signature)

        import hashlib
        md = hashlib.md5()  # 导入md5算法
        md.update(signature_str)  # 把值传给md5算法

        signature_ = md.hexdigest()

        # print('长度: ', len(md.hexdigest()) * 4)

        return signature_

    def get_uri(self):
        '''
        获取access_token的uri
        :return:
        '''
        uri = 'http://your-domain.com/some_path_for_access_token?appid={appid}&nonce={nonce}&signature={signature}&timestamp={timestamp}'
        return uri.format(
            signature=self.signature,
            timestamp=self.timestamp,
            nonce=self.nonce,
            appid=self.appid
        )

    def validate(self, attrs):
        return attrs

    class Meta:
        model = models.AccessToken
        fields = '__all__'

    pass
