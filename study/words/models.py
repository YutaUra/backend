from django.db import models
from study.models import Grade, Subject, TextbookUnit, TextbookChapter
from django.utils.translation import ugettext_lazy as _
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()


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
