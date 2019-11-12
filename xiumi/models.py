import requests
from django.db import models


# Create your models here.


class PartnerUser(models.Model):
    '''
    用户登录入口
    '''
    uid = models.IntegerField(help_text='正整数，小于2的32次方。用户在合作方应用的唯一标识。 由合作方应用提供，秀米将使用其作为用户在秀米的身份标识。')
    route_type = models.CharField(max_length=10, default='article', help_text='登录后使用的功能，当前固定为article，表示“图文编辑器”')
    timestamp = models.IntegerField(help_text='当前UNIX时间戳，单位：秒。')
    appid = models.CharField(max_length=50, help_text='合作方应用在秀米平台的唯一标识，由秀米提前颁发，形式为一个32个字符的字符串。')
    nonce = models.CharField(max_length=10, help_text='随机字符串，由合作方应用在每一次签名时生成，使用于签名算法内。')
    signature = models.CharField(max_length=50, help_text='每次登录时根据各项参数计算得出的签名字符串。算法见下面的说明.')
    pass


class AccessToken(models.Model):
    '''
    获取access_token
    '''
    access_token = models.CharField(max_length=50, null=True, blank=True)
    expires_in = models.IntegerField(help_text='access_token有效的时间，单位是秒', null=True, blank=True)
    code = models.IntegerField(default=0, help_text='为一个非0的整数值，表示发生了错误，具体值的含义没有约定。')
    msg = models.TextField(help_text='用来说明错误原因，可能在页面上显示给用户', null=True, blank=True)


class SomePathForArticles(models.Model):
    '''
    接收图文内容的接口 父级
    '''
    code = models.IntegerField(default=0, help_text='code指示图文是否被正常接收，0表示正常，其他值为异常。')
    msg = models.TextField(help_text='msg是说明文本，提供相关的说明', null=True, blank=True)
    pass


class SomePathForImage(models.Model):
    """
    接收图片文件 父级
    """
    code = models.IntegerField(default=0, help_text='为一个非0的整数值，表示发生了错误，具体值的含义没有约定。')
    msg = models.TextField(help_text='用来说明错误原因，可能在页面上显示给用户', null=True, blank=True)


class SomePathForImageData(models.Model):
    """
    接收图片文件 子级
    """
    url = models.URLField(help_text='图片在合作方的URL')
    name = models.TextField(help_text='图片的名称，在html中可能作为alt显示', null=True, blank=True)
    some_path_for_image_key = models.ForeignKey(SomePathForImage, on_delete=models.CASCADE, null=True, blank=True,
                                                related_name='data')


class SomeArticles(models.Model):
    '''
    接收的图文内容 子级

    from_id是该图文在秀米的唯一编号。description是一个HTML格式的字符串，包含图文内容
    '''

    def get_upload_to(self, filename):
        import os
        import time
        from django.utils import timezone

        now = timezone.now()
        if not timezone.is_naive(now):
            now = timezone.make_naive(now, timezone.utc)

        filename = '{}.{}'.format(
            str(now).split('.')[0],
            filename.split('.')[-1]
        )
        path = os.path.join(
            'media',
            'xiumi',
            "article-image",
            str(time.mktime(now.timetuple())).split('.')[0],
            filename
        )
        return path

    from_id = models.IntegerField(help_text='是该图文在秀米的唯一编号', null=True, blank=True)
    author = models.CharField(max_length=200, help_text='', null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(help_text='是一个HTML格式的字符串，包含图文内容。', null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_to, null=True, blank=True)
    picurl = models.URLField(null=True, blank=True)
    showCover = models.IntegerField(null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    articles_key = models.ForeignKey(SomePathForArticles, on_delete=models.CASCADE, related_name='articles', null=True,
                                     blank=True)

    def download_img(self, img_url):
        from django.core.files import File
        from io import BytesIO
        from django.core.files.base import ContentFile
        from urllib.request import urlopen, urlretrieve

        rs = urlopen(img_url)
        io = BytesIO(rs.read())
        return File(io)
        # return ContentFile(rs.read())

    def save(self, *args, **kwargs):
        # if self.picurl and not self.image:
        #     print('save')
        #     s = self.download_img(self.picurl)
        #     self.image = s
        #     print('self.image', s)
        super(SomeArticles, self).save(*args, **kwargs)
