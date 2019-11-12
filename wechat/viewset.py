from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSetMixin, ModelViewSet
from wechatpy import parse_message
from wechatpy.crypto import WeChatCrypto
from wechatpy.exceptions import InvalidAppIdException, InvalidSignatureException

from wechat.mixin import RequestMixin
from wechat.event.mixins import ListEvent


class GenericWeiChatAPIView(ViewSetMixin, GenericAPIView, RequestMixin):
    pass


class WeiChatEventManagerViewSet(ModelViewSet, RequestMixin, ListEvent):
    '''
    微信事件集成 事件触发
    '''
    wei_message = None
    wei_msg_signature = None
    wei_timestamp = None
    wei_nonce = None
    wei_xml = None
    wei_send_xml = None

    def create(self, request, *args, **kwargs):
        self.wei_msg_signature = self.request.query_params.get('msg_signature')
        self.wei_timestamp = self.request.query_params.get('timestamp')
        self.wei_nonce = self.request.query_params.get('nonce')
        self.wei_xml = self.request.body

        self.wei_message = self.get_http_message()
        self.start_event()
        return HttpResponse(self.wei_send_xml)

    def get_http_message(self):
        '''
        或许WeChat响应体对象
        :return: msg
        '''

        crypto = WeChatCrypto(self.server_token, self.server_encoding_aes_key, self.app_id)
        try:
            decrypted_xml = crypto.decrypt_message(
                self.wei_xml,
                self.wei_msg_signature,
                self.wei_timestamp,
                self.wei_nonce
            )
        except (InvalidAppIdException, InvalidSignatureException):
            # 处理异常或忽略
            return ''

        return parse_message(decrypted_xml)

    def start_event(self):
        '''
        WeChat事件处理
        :return:
        '''
        for item in self.event:
            print('find', item)
            if isinstance(self.wei_message, item.expected_type):
                event_method = item(self.wei_message)
                event_method.on_take()
                self.wei_send_xml = event_method.render()
                continue

    pass
