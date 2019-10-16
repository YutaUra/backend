from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		for user in User.objects.all():
			print(user.pub_id, "\t", end="")
			print(user.nickname if hasattr(user, 'profile') else None, "\t", end="")
			print(user.email)
