from wechatpy import messages, events
from wechatpy.replies import TextReply, EmptyReply


class Event(object):
    '''
    事件基类
    '''

    reply = None
    expected_type = None
    msg_reply = None

    id = 0
    type = 'unknown'  # 消息的类型
    source = None  # 消息的来源用户，即发送消息的用户
    target = None  # 消息的目标用户
    create_time = None  # 消息的发送时间，UNIX 时间戳
    time = None

    def __init__(self, msg):
        if not isinstance(msg, self.expected_type):
            raise TypeError("Expected " + str(self.expected_type))

        self.msg = msg
        self.id = self.msg.id
        self.type = self.msg.type
        self.source = self.msg.source
        self.target = self.msg.target
        self.create_time = self.msg.create_time
        self.time = self.msg.time

    def on_take(self):
        '''
        推送消息-主动调用该方法
        :return:
        '''
        print('TextMessageBase', self.id)
        print('TextMessageBase', self.type)
        print('TextMessageBase', self.source)
        print('TextMessageBase', self.target)
        print('TextMessageBase', self.create_time)
        print('TextMessageBase', self.time)

        context = self.get_reply_body()
        if not context:
            self.msg_reply = EmptyReply()
            print('EmptyReply', type(self.msg_reply))
            return

        context_send = {
            'message': self.msg,
            **context
        }

        self.msg_reply = self.reply(**context_send)

    def get_reply_body(self, context=None):
        '''
        微信公众号消息回复内容构建
        :param context:
        :return:
        '''
        return context

    def render(self):
        return self.msg_reply.render()


class MessageBase(Event):
    '''
    推送信息
    '''
    pass


class EventBase(Event):
    '''
    推送事件
    '''
    event = None

    def __init__(self, msg):
        super(EventBase, self).__init__(msg)
        self.event = self.msg.event

    def on_take(self):
        super(EventBase, self).on_take()
        print('EventBase', self.event)
        return

    pass


class TextMessageBase(MessageBase):
    '''
    文本消息基类
    '''
    reply = TextReply
    content = None  # 信息内容
    expected_type = messages.TextMessage

    def on_take(self):
        super(TextMessageBase, self).on_take()
        self.content = self.msg.content
        print('TextMessageBase', self.content)
        return


class ImageMessageBase(MessageBase):
    '''
    图片消息
    '''
    reply = TextReply
    image = None  # 信息内容
    expected_type = messages.ImageMessage

    def on_take(self):
        super(ImageMessageBase, self).on_take()
        self.image = self.msg.image
        print('ImageMessageBase', self.image)
        return

    def get_reply_body(self, context=None):
        return super(ImageMessageBase, self).get_reply_body(context={
            'content': '图片消息'
        })


class VoiceMessageBase(MessageBase):
    '''
    语音消息
    '''
    reply = TextReply
    expected_type = messages.VoiceMessage
    media_id = None  # 微信内部的一个文件 ID
    format = None  # 声音文件格式
    recognition = None  # 语音识别结果(启用了语音识别时才有)

    def on_take(self):
        super(VoiceMessageBase, self).on_take()
        self.media_id = self.msg.media_id
        self.format = self.msg.format
        self.recognition = self.msg.recognition
        print('VoiceMessageBase', self.media_id)
        print('VoiceMessageBase', self.format)
        print('VoiceMessageBase', self.recognition)
        return

    def get_reply_body(self, context=None):
        return super(VoiceMessageBase, self).get_reply_body(context={
            'content': '语音消息'
        })


class VideoMessageBase(MessageBase):
    '''
    视频消息
    '''
    reply = TextReply
    expected_type = messages.VideoMessage
    media_id = None  # 微信内部的一个文件 ID
    thumb_media_id = None  # 视频缩略图文件 ID

    def on_take(self):
        super(VideoMessageBase, self).on_take()
        self.media_id = self.msg.media_id
        self.thumb_media_id = self.msg.thumb_media_id

        print('VideoMessageBase', self.media_id)
        print('VideoMessageBase', self.thumb_media_id)
        return

    def get_reply_body(self, context=None):
        return super(VideoMessageBase, self).get_reply_body(context={
            'content': '视频消息'
        })


class LocationMessageBase(MessageBase):
    '''
    地理位置消息
    '''
    reply = TextReply
    expected_type = messages.LocationMessage
    location_x = None  # 地理位置纬度
    location_y = None  # 地理位置经度
    scale = None  # 地图缩放大小
    label = None  # 地理位置信息
    location = None  # (纬度, 经度) 元组

    def on_take(self):
        super(LocationMessageBase, self).on_take()

        self.location_x = self.msg.location_x
        self.location_y = self.msg.location_y
        self.scale = self.msg.scale
        self.label = self.msg.label
        self.location = self.msg.location

        print('LocationMessageBase', self.location_x)
        print('LocationMessageBase', self.location_y)
        print('LocationMessageBase', self.scale)
        print('LocationMessageBase', self.label)
        print('LocationMessageBase', self.location)
        return

    def get_reply_body(self, context=None):
        return super(LocationMessageBase, self).get_reply_body(context={
            'content': '地理位置消息'
        })


class LinkMessageBase(MessageBase):
    '''
    链接消息
    '''
    reply = TextReply
    expected_type = messages.LinkMessage
    title = None  # 链接标题
    description = None  # 链接描述
    url = None  # 链接地址

    def on_take(self):
        super(LinkMessageBase, self).on_take()

        self.title = self.msg.title
        self.description = self.msg.description
        self.url = self.msg.url

        print('LinkMessageBase', self.title)
        print('LinkMessageBase', self.description)
        print('LinkMessageBase', self.url)
        return

    def get_reply_body(self, context=None):
        return super(LinkMessageBase, self).get_reply_body(context={
            'content': '链接消息'
        })


class ShortVideoMessageBase(MessageBase):
    '''
    短视频消息
    '''
    reply = TextReply
    expected_type = messages.ShortVideoMessage
    media_id = None  # 短视频 media_id
    thumb_media_id = None  # 短视频缩略图 media_id

    def on_take(self):
        super(ShortVideoMessageBase, self).on_take()

        self.media_id = self.msg.media_id
        self.thumb_media_id = self.msg.thumb_media_id

        print('ShortVideoMessageBase', self.media_id)
        print('ShortVideoMessageBase', self.thumb_media_id)
        return

    def get_reply_body(self, context=None):
        return super(ShortVideoMessageBase, self).get_reply_body(context={
            'content': '短视频消息'
        })


class SubscribeEventBase(EventBase):
    '''
    关注事件
    '''
    reply = TextReply
    expected_type = events.SubscribeEvent

    def get_reply_body(self, context=None):
        return super(SubscribeEventBase, self).get_reply_body(context={
            'content': '关注事件'
        })


class UnsubscribeEventBase(EventBase):
    '''
    取消关注事件
    '''
    reply = TextReply
    expected_type = events.UnsubscribeEvent

    def get_reply_body(self, context=None):
        return super(UnsubscribeEventBase, self).get_reply_body(context={
            'content': '取消关注事件'
        })


class SubscribeScanEventBase(EventBase):
    '''
    取消关注事件
    '''
    reply = TextReply
    expected_type = events.SubscribeScanEvent

    def get_reply_body(self, context=None):
        return super(SubscribeScanEventBase, self).get_reply_body(context={
            'content': '取消关注事件'
        })


class ScanEventBase(EventBase):
    '''
    未关注用户扫描带参数二维码事件
    '''
    reply = TextReply
    expected_type = events.ScanEvent

    def get_reply_body(self, context=None):
        return super(ScanEventBase, self).get_reply_body(context={
            'content': '未关注用户扫描带参数二维码事件'
        })


class LocationEventBase(EventBase):
    '''
    已关注用户扫描带参数二维码事件
    '''
    reply = TextReply
    expected_type = events.LocationEvent

    def get_reply_body(self, context=None):
        return super(LocationEventBase, self).get_reply_body(context={
            'content': '已关注用户扫描带参数二维码事件'
        })


class ClickEventBase(EventBase):
    '''
    上报地理位置事件
    '''
    reply = TextReply
    expected_type = events.ClickEvent

    def get_reply_body(self, context=None):
        return super(ClickEventBase, self).get_reply_body(context={
            'content': '上报地理位置事件'
        })


class ViewEventBase(EventBase):
    '''
    点击菜单拉取消息事件
    '''
    reply = TextReply
    expected_type = events.ViewEvent

    def get_reply_body(self, context=None):
        return super(ViewEventBase, self).get_reply_body(context={
            'content': '点击菜单拉取消息事件'
        })


class MassSendJobFinishEventBase(EventBase):
    '''
    群发消息发送任务完成事件
    '''
    reply = TextReply
    expected_type = events.MassSendJobFinishEvent

    def get_reply_body(self, context=None):
        return super(MassSendJobFinishEventBase, self).get_reply_body(context={
            'content': '群发消息发送任务完成事件'
        })


class TemplateSendJobFinishEventBase(EventBase):
    '''
    模板消息发送任务完成事件
    '''
    reply = TextReply
    expected_type = events.TemplateSendJobFinishEvent

    def get_reply_body(self, context=None):
        return super(TemplateSendJobFinishEventBase, self).get_reply_body(context={
            'content': '模板消息发送任务完成事件'
        })


class ScanCodePushEventBase(EventBase):
    '''
    扫码推事件
    '''
    reply = TextReply
    expected_type = events.ScanCodePushEvent

    def get_reply_body(self, context=None):
        return super(ScanCodePushEventBase, self).get_reply_body(context={
            'content': '扫码推事件'
        })


class ScanCodeWaitMsgEventBase(EventBase):
    '''
    扫码推事件且弹出“消息接收中”提示框
    '''
    reply = TextReply
    expected_type = events.ScanCodeWaitMsgEvent

    def get_reply_body(self, context=None):
        return super(ScanCodeWaitMsgEventBase, self).get_reply_body(context={
            'content': '扫码推事件且弹出“消息接收中”提示框'
        })


class PicSysPhotoEventBase(EventBase):
    '''
    弹出系统拍照发图事件
    '''
    reply = TextReply
    expected_type = events.PicSysPhotoEvent

    def get_reply_body(self, context=None):
        return super(PicSysPhotoEventBase, self).get_reply_body(context={
            'content': '弹出系统拍照发图事件'
        })


class PicPhotoOrAlbumEventBase(EventBase):
    '''
    弹出拍照或者相册发图事件
    '''
    reply = TextReply
    expected_type = events.PicPhotoOrAlbumEvent

    def get_reply_body(self, context=None):
        return super(PicPhotoOrAlbumEventBase, self).get_reply_body(context={
            'content': '弹出拍照或者相册发图事件'
        })


class PicWeChatEventBase(EventBase):
    '''
    弹出微信相册发图器事件
    '''
    reply = TextReply
    expected_type = events.PicWeChatEvent

    def get_reply_body(self, context=None):
        return super(PicWeChatEventBase, self).get_reply_body(context={
            'content': '弹出微信相册发图器事件'
        })


class LocationSelectEventBase(EventBase):
    '''
    弹出地理位置选择器事件
    '''
    reply = TextReply
    expected_type = events.LocationSelectEvent

    def get_reply_body(self, context=None):
        return super(LocationSelectEventBase, self).get_reply_body(context={
            'content': '弹出地理位置选择器事件'
        })


class QualificationVerifySuccessEventBase(EventBase):
    '''
    微信认证事件推送-资质认证成功事件
    '''
    reply = TextReply
    expected_type = events.QualificationVerifySuccessEvent

    def get_reply_body(self, context=None):
        return super(QualificationVerifySuccessEventBase, self).get_reply_body(context={
            'content': '微信认证事件推送-资质认证成功事件'
        })


class QualificationVerifyFailEventBase(EventBase):
    '''
    微信认证事件推送-资质认证失败事件
    '''
    reply = TextReply
    content = None  # 信息内容
    expected_type = events.QualificationVerifyFailEvent

    def get_reply_body(self, context=None):
        return super(QualificationVerifyFailEventBase, self).get_reply_body(context={
            'content': '微信认证事件推送-资质认证失败事件'
        })


class NamingVerifySuccessEventBase(EventBase):
    '''
    微信认证事件推送-名称认证成功
    '''
    reply = TextReply
    expected_type = events.NamingVerifySuccessEvent

    def get_reply_body(self, context=None):
        return super(NamingVerifySuccessEventBase, self).get_reply_body(context={
            'content': '微信认证事件推送-名称认证成功'
        })


class NamingVerifyFailEventBase(EventBase):
    '''
    微信认证事件推送-名称认证失败
    '''
    reply = TextReply
    expected_type = events.NamingVerifyFailEvent

    def get_reply_body(self, context=None):
        return super(NamingVerifyFailEventBase, self).get_reply_body(context={
            'content': '微信认证事件推送-名称认证失败'
        })


class AnnualRenewEventBase(EventBase):
    '''
    微信认证事件推送-年审通知
    '''
    reply = TextReply
    expected_type = events.AnnualRenewEvent

    def get_reply_body(self, context=None):
        return super(AnnualRenewEventBase, self).get_reply_body(context={
            'content': '微信认证事件推送-年审通知'
        })


class VerifyExpiredEventBase(EventBase):
    '''
    微信认证事件推送-认证过期失效通知
    '''
    reply = TextReply
    expected_type = events.VerifyExpiredEvent

    def get_reply_body(self, context=None):
        return super(VerifyExpiredEventBase, self).get_reply_body(context={
            'content': '微信认证事件推送-认证过期失效通知'
        })


class UserScanProductEventBase(EventBase):
    '''
    微信扫一扫事件-打开商品主页事件
    '''
    reply = TextReply
    expected_type = events.UserScanProductEvent

    def get_reply_body(self, context=None):
        return super(UserScanProductEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-打开商品主页事件'
        })


class UserScanProductEnterSessionEventBase(EventBase):
    '''
    微信扫一扫事件-进入公众号事件
    '''
    reply = TextReply
    expected_type = events.UserScanProductEnterSessionEvent

    def get_reply_body(self, context=None):
        return super(UserScanProductEnterSessionEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-进入公众号事件'
        })


class UserScanProductAsyncEventBase(EventBase):
    '''
    微信扫一扫事件-地理位置信息异步推送事件
    '''
    reply = TextReply
    expected_type = events.UserScanProductAsyncEvent

    def get_reply_body(self, context=None):
        return super(UserScanProductAsyncEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-地理位置信息异步推送事件'
        })


class UserScanProductVerifyActionEventBase(EventBase):
    '''
    微信扫一扫事件-商品审核结果事件
    '''
    reply = TextReply
    expected_type = events.UserScanProductVerifyActionEvent

    def get_reply_body(self, context=None):
        return super(UserScanProductVerifyActionEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-商品审核结果事件'
        })

    pass


class SubscribeScanProductEventBase(EventBase):
    '''
    微信扫一扫事件-当用户在商品主页中关注公众号事件
    '''
    reply = TextReply
    expected_type = events.SubscribeScanEvent

    def get_reply_body(self, context=None):
        return super(SubscribeScanProductEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-当用户在商品主页中关注公众号事件'
        })


class UserAuthorizeInvoiceEventBase(EventBase):
    '''
    微信扫一扫事件-用户授权发票事件
    '''
    reply = TextReply
    expected_type = events.UserAuthorizeInvoiceEvent

    def get_reply_body(self, context=None):
        return super(UserAuthorizeInvoiceEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-用户授权发票事件'
        })


class UpdateInvoiceStatusEventBase(EventBase):
    '''
    微信扫一扫事件-发票状态更新事件
    '''
    reply = TextReply
    expected_type = events.UpdateInvoiceStatusEvent

    def get_reply_body(self, context=None):
        return super(UpdateInvoiceStatusEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-发票状态更新事件'
        })


class SubmitInvoiceTitleEventBase(EventBase):
    '''
    微信扫一扫事件-用户提交发票抬头事件
    '''
    reply = TextReply
    expected_type = events.SubmitInvoiceTitleEvent

    def get_reply_body(self, context=None):
        return super(SubmitInvoiceTitleEventBase, self).get_reply_body(context={
            'content': '微信扫一扫事件-用户提交发票抬头事件'
        })
