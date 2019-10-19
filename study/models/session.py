from django.db import models
from django.utils.datetime_safe import datetime

from users.models import User

import uuid
from study.base_session import BaseSession, BaseSessionManager


class StudySessionManager(BaseSessionManager):
    pass


class StudySession(BaseSession):
    objects = BaseSessionManager()
