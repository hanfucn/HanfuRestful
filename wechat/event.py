from wechatpy import messages, events
from wechatpy.replies import TextReply, EmptyReply

from wechat.event import base


class TextMessage(base.TextMessageBase):
    """
    文本消息基类
    """


class ImageMessage(base.ImageMessageBase):
    """
    图片消息
    """


class VoiceMessage(base.VoiceMessageBase):
    """
    语音消息
    """


class VideoMessage(base.VideoMessageBase):
    """
    视频消息
    """


class LocationMessage(base.LocationMessageBase):
    """
    地理位置消息
    """


class LinkMessage(base.LinkMessageBase):
    """
    链接消息
    """


class ShortVideoMessage(base.ShortVideoMessageBase):
    """
    短视频消息
    """


class SubscribeEvent(base.SubscribeEventBase):
    """
    关注事件
    """


class UnsubscribeEvent(base.UnsubscribeEventBase):
    """
    取消关注事件
    """


class SubscribeScanEvent(base.SubscribeScanEventBase):
    """
    取消关注事件
    """


class ScanEvent(base.ScanEventBase):
    """
    未关注用户扫描带参数二维码事件
    """


class LocationEvent(base.LocationEventBase):
    """
    已关注用户扫描带参数二维码事件
    """


class ClickEvent(base.ClickEventBase):
    """
    上报地理位置事件
    """


class ViewEvent(base.ViewEventBase):
    """
    点击菜单拉取消息事件
    """


class MassSendJobFinishEvent(base.MassSendJobFinishEventBase):
    """
    群发消息发送任务完成事件
    """


class TemplateSendJobFinishEvent(base.TemplateSendJobFinishEventBase):
    """
    模板消息发送任务完成事件
    """


class ScanCodePushEvent(base.ScanCodePushEventBase):
    """
    扫码推事件
    """


class ScanCodeWaitMsgEvent(base.ScanCodeWaitMsgEventBase):
    """
    扫码推事件且弹出“消息接收中”提示框
    """


class PicSysPhotoEvent(base.PicSysPhotoEventBase):
    """
    弹出系统拍照发图事件
    """


class PicPhotoOrAlbumEvent(base.PicPhotoOrAlbumEventBase):
    """
    弹出拍照或者相册发图事件
    """


class PicWeChatEvent(base.PicWeChatEventBase):
    """
    弹出微信相册发图器事件
    """


class LocationSelectEvent(base.LocationSelectEventBase):
    """
    弹出地理位置选择器事件
    """


class QualificationVerifySuccessEvent(base.QualificationVerifySuccessEventBase):
    """
    微信认证事件推送-资质认证成功事件
    """


class QualificationVerifyFailEvent(base.QualificationVerifyFailEventBase):
    """
    微信认证事件推送-资质认证失败事件
    """


class NamingVerifySuccessEvent(base.NamingVerifySuccessEventBase):
    """
    微信认证事件推送-名称认证成功
    """


class NamingVerifyFailEvent(base.NamingVerifyFailEventBase):
    """
    微信认证事件推送-名称认证失败
    """


class AnnualRenewEvent(base.AnnualRenewEventBase):
    """
    微信认证事件推送-年审通知
    """


class VerifyExpiredEvent(base.VerifyExpiredEventBase):
    """
    微信认证事件推送-认证过期失效通知
    """


class UserScanProductEvent(base.UserScanProductEventBase):
    """
    微信扫一扫事件-打开商品主页事件
    """


class UserScanProductEnterSessionEvent(base.UserScanProductEnterSessionEventBase):
    """
    微信扫一扫事件-进入公众号事件
    """


class UserScanProductAsyncEvent(base.UserScanProductAsyncEventBase):
    """
    微信扫一扫事件-地理位置信息异步推送事件
    """


class UserScanProductVerifyActionEvent(base.UserScanProductVerifyActionEventBase):
    """
    微信扫一扫事件-商品审核结果事件
    """


class SubscribeScanProductEvent(base.SubscribeScanProductEventBase):
    """
    微信扫一扫事件-当用户在商品主页中关注公众号事件
    """


class UserAuthorizeInvoiceEvent(base.UserAuthorizeInvoiceEventBase):
    """
    微信扫一扫事件-用户授权发票事件
    """


class UpdateInvoiceStatusEvent(base.UpdateInvoiceStatusEventBase):
    """
    微信扫一扫事件-发票状态更新事件
    """


class SubmitInvoiceTitleEvent(base.SubmitInvoiceTitleEventBase):
    """
    微信扫一扫事件-用户提交发票抬头事件
    """
