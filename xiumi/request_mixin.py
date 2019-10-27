import requests

from hanfurestful import settings
from xiumi.mixins import XiuMiMixin


class AccessTokenMixin(XiuMiMixin):
    # url = ''
    # payload = {}
    url = 'http://your-domain.com/some_path_for_access_token?'  # appid={appid}&nonce={nonce}&signature={signature}&timestamp={timestamp}

    def re_get(self):
        params = {
            'appid': self.app_id,
            'nonce': self.nonce,
            'signature': self.get_access_token_signature(),
            'timestamp': self.timestamp
        }
        _re = requests.get(url=self.url, params=params)
        print(_re.text)
        return _re.json()

    pass
