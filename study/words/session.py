from django.db import models
from study.base_session import BaseSubSession, BaseSessionItem
from study.models import StudySession
from study.words import Word
from study.words.models import Mode


class WordSession(BaseSubSession):
    session = models.ForeignKey(to=StudySession, on_delete=models.PROTECT, blank=True)


class WordGet(BaseSessionItem):
    sub_session = models.ForeignKey(to=WordSession, on_delete=models.PROTECT, blank=True)
    get_range = models.CharField(max_length=100, blank=True, null=True)


class WordPractice(BaseSessionItem):
    mode = models.ForeignKey(to=Mode, on_delete=models.PROTECT, blank=True, null=True)
    sub_session = models.ForeignKey(to=WordSession, on_delete=models.PROTECT, blank=True)
    word = models.ForeignKey(to=Word, on_delete=models.PROTECT, related_name='word')
    answer = models.ForeignKey(to=Word, on_delete=models.PROTECT, related_name='answer')
