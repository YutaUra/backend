from django.db import models
from study.models import Subject, TextbookUnit, TextbookChapter
from django.utils.translation import ugettext_lazy as _
import uuid
from django.contrib.auth import get_user_model
from django.db.models import Count, F, FloatField, ExpressionWrapper, Q
from django.db.models.functions import Cast

User = get_user_model()


class WordManager(models.Manager):
    def _words_score(self, **kwargs):
        return self.filter(**kwargs).annotate(
            score=ExpressionWrapper(
                (Cast(Count('answer', filter=(Q(answer=F('word')))) + 1, FloatField())) /
                (Cast(Count('answer') + 2, FloatField())),
                FloatField()
            )).order_by('score')

    def review_words(self, user, mode, count=20):
        print(self.filter(word__mode=mode, word__user=user))
        return self._words_score(word__user=user, word__mode=mode)[:count]


class Word(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT)
    name = models.CharField(
        _('言葉'),
        max_length=100,
    )
    mean = models.CharField(
        _('意味'),
        max_length=100,
    )
    objects = WordManager()

    def __str__(self):
        return 'word %s' % self.name


class TextbookWord(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    textbook_unit = models.ForeignKey(to=TextbookUnit, on_delete=models.PROTECT)
    textbook_chapter = models.ForeignKey(to=TextbookChapter, on_delete=models.PROTECT, blank=True, null=True)
    word = models.ForeignKey(to=Word, on_delete=models.PROTECT)


class Mode(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=100)
