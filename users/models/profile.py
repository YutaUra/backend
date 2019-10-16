from django.conf import settings
import os
import random
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .profile_manager import ProfileManager

GENDER = (
    ("F", "女性"),
    ("M", "男性"),
)


def get_icons_list():
    icon_dir = os.path.join(settings.BASE_DIR, 'staticfiles', 'user_icons')
    return [(file_name,
             file_name.split('.')[0].split('-')[1]
             ) for file_name in os.listdir(icon_dir)]


icons = get_icons_list()


def get_random_icon():
    icon_list = get_icons_list()
    return random.choice(icon_list)[0]


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    icon = models.CharField(
        choices=icons,
        default=get_random_icon,
        max_length=100,
    )
    nickname = models.CharField(
        _("ニックネーム"),
        max_length=255,
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    phone = models.CharField(
        _("電話番号"),
        max_length=255,
        blank=True,
    )
    gender = models.CharField(
        _("性別"),
        max_length=2,
        choices=GENDER,
        blank=True,
    )
    objects = ProfileManager()

    def __str__(self):
        return self.nickname

    @property
    def full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
