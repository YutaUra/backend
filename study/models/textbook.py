from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from .grade import Grade
from .subjects import Subject
from .unit import Unit


class Textbook(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    grade = models.ForeignKey(to=Grade, on_delete=models.PROTECT)
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT)
    publisher = models.CharField(
        _('出版社'),
        max_length=20,
        blank=True,
    )
    name = models.CharField(
        _("教科書名"),
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.name


class TextbookUnit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    textbook = models.ForeignKey(to=Textbook, on_delete=models.PROTECT)
    unit = models.ManyToManyField(to=Unit)
    name = models.CharField(
        _("単元名"),
        max_length=100,
    )

    def __str__(self):
        return self.name


class TextbookChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    textbook_unit = models.ForeignKey(to=TextbookUnit, on_delete=models.PROTECT)
    unit = models.ManyToManyField(to=Unit, blank=True)
    name = models.CharField(
        _('章'),
        max_length=100,
    )

    def __str__(self):
        return '%s %s' % (self.textbook_unit, self.name)
