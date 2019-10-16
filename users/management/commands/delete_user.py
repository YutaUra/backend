from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
	help = 'Delete users'

	def add_arguments(self, parser):
		parser.add_argument('email', nargs='+', type=str, help='User ID')

	def handle(self, *args, **kwargs):
		users_ids = kwargs['email']
		if users_ids[0] == "all":
			users = User.objects.all()
			users_pub_ids = [user.pub_is for user in users]
		else:
			users_pub_ids = users_ids

		for pub_id in users_pub_ids:
			try:
				user = User.objects.get(pub_id=pub_id)
				user.delete()
				self.stdout.write('User "%s (%s)" deleted with success!' % (user.username, pub_id))
			except User.DoesNotExist:
				self.stdout.write('User with id "%s" does not exist.' % pub_id)
