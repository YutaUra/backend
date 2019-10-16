from django.db import models
from uuid import UUID
from users.models import User


class ProfileQuerySet(models.QuerySet):

    def filter(self, *args, **kwargs):
        if "pk" in kwargs:
            pk = kwargs["pk"]
            if self.is_uuid(pk):
                """
                this pk is caused by user
                """
                user = User.objects.get(pub_id=pk)
                pk = user.profile.pk
                kwargs["pk"] = pk
        return super().filter(*args, **kwargs)

    @staticmethod
    def is_uuid(uuid_string):
        """
        Validation for uuid or just a string
        :param uuid_string: str
        :return: bool
        """
        try:
            UUID(str(uuid_string), version=4)
        except ValueError:
            """
            can`t convert string to uuid
            """
            return False
        return True


class ProfileManager(models.Manager):
    use_in_migrations = True

    def get_queryset(self):
        return ProfileQuerySet(self.model, using=self._db)
