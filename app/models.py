from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    """用户"""

    # fixme

    class Meta(AbstractUser.Meta):
        ordering = ['-date_joined']
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """验证码"""

    # fixme

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = "验证码"

    def __str__(self):
        pass
