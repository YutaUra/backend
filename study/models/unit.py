from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from .grade import Grade
from .subjects import Subject


class Unit(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    grade = models.ForeignKey(to=Grade, on_delete=models.PROTECT, )
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT,)
    parent = models.ManyToManyField(to='self', verbose_name='親単元', blank=True)
    name = models.CharField(
        _("単元名"),
        max_length=20,
    )

    class Meta:
        ordering = [models.F('grade').desc(nulls_last=True)]

    def __str__(self):
        return '%s %s' % (self.grade, self.name)
