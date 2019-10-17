from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        groups = []
        for name in ['teacher', 'student']:
            if Group.objects.filter(name=name):
                continue
            else:
                groups.append(Group(name=name))
        Group.objects.bulk_create(groups)
