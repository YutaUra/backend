from django.db import models
from users.models import User
from django.utils import timezone


class FollowRelation(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='follows',
        to_field='pub_id',
    )
    follow_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='follower',
        to_field='pub_id',
    )
    followed_at = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return f'{self.user} follows {self.follow_user}'

