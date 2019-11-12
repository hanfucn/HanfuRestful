from wechatpy import messages

from wechat.event import base


class ListEvent(object):
    '''
    事件注册
    '''
    event = [
        base.TextMessageBase,
        base.ImageMessageBase,
        base.VoiceMessageBase,
        base.VideoMessageBase,
        base.LocationMessageBase,
        base.LinkMessageBase,
        base.ShortVideoMessageBase,
        base.SubscribeEventBase,
        base.UnsubscribeEventBase,
        base.SubscribeScanEventBase,
        base.ScanEventBase,
        base.LocationEventBase,
        base.ClickEventBase,
        base.ViewEventBase,
        base.MassSendJobFinishEventBase,
        base.TemplateSendJobFinishEventBase,
        base.ScanCodePushEventBase,
        base.ScanCodeWaitMsgEventBase,
        base.PicSysPhotoEventBase,
        base.PicPhotoOrAlbumEventBase,
        base.PicWeChatEventBase,
        base.LocationSelectEventBase,
        base.QualificationVerifySuccessEventBase,
        base.QualificationVerifyFailEventBase,
        base.NamingVerifySuccessEventBase,
        base.NamingVerifyFailEventBase,
        base.AnnualRenewEventBase,
        base.VerifyExpiredEventBase,
        base.UserScanProductEventBase,
        base.UserScanProductEnterSessionEventBase,
        base.UserScanProductAsyncEventBase,
        base.UserScanProductVerifyActionEventBase,
        base.SubscribeScanProductEventBase,
        base.UserAuthorizeInvoiceEventBase,
        base.UpdateInvoiceStatusEventBase,
        base.SubmitInvoiceTitleEventBase
    ]
