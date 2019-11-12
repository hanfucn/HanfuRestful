from hanfurestful import settings


class RequestMixin:
    '''

    '''
    # 公众号的唯一标识
    app_id = settings.WEI_XIN.get('APP_ID')
    app_secret = settings.WEI_XIN.get('APP_SECRET')
    server_token = settings.WEI_XIN.get('APP_TOKEN')
    server_encoding_aes_key = settings.WEI_XIN.get('APP_DES_KEY')
    redirect_uri = settings.WEI_XIN.get('APP_REDIRECT_URI')

    response_type = 'code'

    '''
    应用授权作用域
    snsapi_base： 不弹出授权页面，直接跳转，只能获取用户openid
    snsapi_userinfo： 弹出授权页面，可通过openid拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息
    '''
    scope = 'snsapi_userinfo'

    # 重定向后会带上state参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
    state = ''

    access_grant_type = 'client_credential'
    access_token = ''
    access_uri = 'https://api.weixin.qq.com/cgi-bin/token?grant_type={grant_type}&appid={appid}&secret={appsecret}'.format(
        appid=app_id,
        appsecret=app_secret,
        grant_type=access_grant_type
    )
