from django.db import models

# Create your models here.
from account.models import User


class Article(models.Model):
    '''
    论坛文章
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
            "article-image",
            str(time.mktime(now.timetuple())).split('.')[0],
            filename
        )
        return path

    name = models.CharField(default='C', max_length=255, help_text='记录论坛文章的标题', verbose_name='标题')
    text = models.TextField(default='C', help_text='记录论坛文章内容', verbose_name='内容')
    images = models.ImageField(help_text='记录文章封面图', verbose_name='封面图', upload_to=get_upload_to, null=True)
    verify = models.BooleanField(default=False, help_text='记录文章发布后[是否需要|是否完成]审核', verbose_name='审核')
    create_date = models.DateTimeField(auto_now_add=True, help_text='记录文章创建时间', verbose_name='创建时间')
    change_date = models.DateTimeField(auto_now=True, help_text='记录文章更新时间', verbose_name='更新时间')
    browse = models.IntegerField(default=0, help_text='记录文章浏览量', verbose_name='浏览量')
    user = models.ForeignKey(User, help_text='记录文章创建作者', verbose_name='创建者', on_delete=models.SET_NULL, null=True)


class Activity_Attend(models.Model):
    '''
    报名参加人员信息[活动召集]
    '''
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, help_text='用户所参加的活动', verbose_name='参加的活动')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text='参加者', verbose_name='参加者')
    create_date = models.DateTimeField(auto_now_add=True, help_text='记录活动参加的时间', verbose_name='参加时间')
    pass


class Activity(models.Model):
    '''
    活动召集
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
            "activity-image",
            str(time.mktime(now.timetuple())).split('.')[0],
            filename
        )
        return path

    name = models.CharField(max_length=255, help_text='记录活动的标题', verbose_name='标题')
    text = models.TextField(help_text='记录论坛活动内容', verbose_name='内容')
    images = models.ImageField(help_text='记录活动封面图', verbose_name='封面图', upload_to=get_upload_to)
    place = models.CharField(max_length=255, help_text='记录活动地点', verbose_name='活动地点')
    verify = models.BooleanField(default=False, help_text='记录活动发布后[是否需要|是否完成]审核', verbose_name='审核')
    start_date = models.DateTimeField(help_text='记录活动开始时间', verbose_name='开始时间')
    end_date = models.DateTimeField(help_text='记录活动结束时间', verbose_name='结束时间')
    create_date = models.DateTimeField(auto_now_add=True, help_text='记录活动创建时间', verbose_name='创建时间')
    change_date = models.DateTimeField(auto_now=True, help_text='记录活动更新时间', verbose_name='更新时间')
    browse = models.IntegerField(default=0, help_text='记录活动浏览量', verbose_name='浏览量')
    user_attend = models.ManyToManyField(User, related_name='activity_user_attend', through=Activity_Attend,
                                         help_text='记录活动参加人员', verbose_name='报名人员')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='activity_user',
                             help_text='记录活动创建作者', verbose_name='创建者')
