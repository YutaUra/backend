from django.db import models
from django.utils import timezone
from users.models import User
import uuid


class BaseSessionManager(models.Manager):
    use_in_migrations = True

    def create_or_get_current_session(self, user, **kwargs):
        if isinstance(user, User):
            user_query = self.get_queryset().filter(user=user, **kwargs)
        else:
            # AnonymousUser
            obj = self.model(**kwargs)
            obj.save()
            return obj
        if user_query:
            session = user_query.latest('updated_at')
        else:
            obj = self.model(user=user, **kwargs)
            obj.save()
            return obj
        # 最後の利用から1時間経過している場合は新しいセッションを作成する
        diff = timezone.now() - session.updated_at
        if diff.days > 0 or diff.seconds > 3600:
            obj = self.model(user=user, **kwargs)
            obj.save()
            return obj
        else:
            # uploaded_at の更新
            session.save()
            return session


class BaseSession(models.Model):
    """
    id,user, created_at, uploaded_at
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BaseSessionManager()

    class Meta:
        abstract = True


class BaseSubSession(BaseSession):
    """
    id,user.session, created_at, uploaded_at
    """
    session = models.ForeignKey(to=BaseSession, on_delete=models.PROTECT)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # sessionの更新
        super().save(force_insert, force_update, using, update_fields)
        self.session.save()

    class Meta:
        abstract = True


class BaseSessionItem(models.Model):
    """id, user, sub_session, created_at"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, blank=True, null=True)
    sub_session = models.ForeignKey(to=BaseSubSession, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.sub_session.save()

    class Meta:
        abstract = True
