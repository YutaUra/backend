from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(
        _("教科名"),
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.name
