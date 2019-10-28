from django.conf import settings
from django.core.management import BaseCommand
from django.db.models.functions import datetime
from django.template.loader import get_template

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.filter(_position='S')
        today = datetime.datetime.today()
        today_min = datetime.datetime.combine(today, today.time().min)
        today_max = datetime.datetime.combine(today, today.time().min)
        users = users.exclude(studysession__created_at__range=(today_min, today_max))

        context = {
            'protocol': settings.FRONTEND_POINT.get('PROTOCOL'),
            'domain': settings.FRONTEND_POINT.get('DOMAIN'),
            'site_name': settings.SITE_NAME,
        }

        subject_template = get_template('study/no_session/subject.txt')
        message_template = get_template('study/no_session/body.txt')
        for user in users:
            context.update({'user': user})
            subject = subject_template.render(context)
            message = message_template.render(context)
            user.email_user(subject, message)
