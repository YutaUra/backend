from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserQuerySet(models.QuerySet):
    def follows(self, pub_id):
        return self.filter(follower__user=pub_id)

    def follower(self, pub_id):
        return self.filter(follows__follow_user=pub_id)


class UserManager(BaseUserManager):
    """ユーザーマナージャー"""

    use_in_migrations = True

    # def get_queryset(self):
    # 	return UserQuerySer(self.model, using=self._db)

    def _create_user(self, email, password, **extra_fields):
        from users.models import Profile
        """メールアドレスでの登録を必須にする"""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        profile = Profile()
        profile.user = user
        profile.save()
        return user

    def create_user(self, email, password=None, **extrafields):
        """is_staff, is_superuserをFalseにする"""
        extrafields.setdefault("is_staff", False)
        extrafields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extrafields)

    def create_superuser(self, email, password, **extrafields):
        """is_staff, is_superuserをTrueにする"""
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)

        if extrafields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extrafields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extrafields)

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def follows(self, pub_id):
        return self.get_queryset().follows(pub_id)

    def follower(self, pub_id):
        return self.get_queryset().follower(pub_id)

    def is_exist_id(self, pub_id):
        return pub_id in self.get_queryset().values_list('pub_id', flat=True)

    def is_exist_email(self, email):
        return email in self.get_queryset().values_list('email', flat=True)