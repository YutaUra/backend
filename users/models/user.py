from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, Group
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .user_manager import UserManager
import uuid
from uuid import UUID

from json import JSONEncoder

JSONEncoder_old_default = JSONEncoder.default


def JSONEncoder_new_default(self, o):
    if isinstance(o, UUID):
        return str(o)
    return JSONEncoder_old_default(self, o)


JSONEncoder.default = JSONEncoder_new_default


def str_uuid():
    return str(uuid.uuid4())


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""

    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(_('email address'), unique=True, )
    pub_id = models.CharField(
        _("ID"),
        max_length=50,
        unique=True,
        default=str_uuid,
    )
    _position = models.CharField(
        _("生徒か先生か"),
        choices=(
            ("S", "生徒"),
            ("T", "先生"),
        ),
        max_length=1,
        default="N"
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_user_position(self):
        return self._position

    @property
    def username(self):
        """username属性のゲッター

        他アプリケーションが、username属性にアクセスした場合に備えて定義
        メールアドレスを返す
        """
        return self.email

    @property
    def nickname(self):
        try:
            return self.profile.nickname or self.email
        except Exception:
            return self.email

    @property
    def icon(self):
        try:
            return self.profile.icon
        except Exception:
            return None

    def get_follows(self):
        return User.objects.follows(self.pub_id)

    def get_follower(self):
        return User.objects.follower(self.pub_id)

    def get_is_following(self, user):
        return self in user.get_follows()

    def __str__(self):
        return self.pub_id
