from django.contrib.auth.backends import ModelBackend, UserModel


class EmailAuthBackend(ModelBackend):
    '''邮箱认证登录'''

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel._default_manager.get(email=username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except UserModel.DoesNotExist:
            return super(EmailAuthBackend, self).authenticate(request, username=username, password=password, **kwargs)
