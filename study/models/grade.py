from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class School(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(
        _('小学、中学、高校、大学(修士・博士）'),
        max_length=2,
        unique=True,
    )

    class Meta:
        ordering = [
            'name'
        ]

    def __str__(self):
        return self.name


class Grade(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    school = models.ForeignKey(to=School, on_delete=models.PROTECT,)
    name = models.CharField(
        _("学年(半角数字)"),
        max_length=1,
    )

    class Meta:
        ordering = [
            'school',
            'name'
        ]

    def __str__(self):
        return '%s %s年' % (self.school, self.name)
