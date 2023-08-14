from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import Notification


class Command(BaseCommand):
    help = 'Create a new notification'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user')
        parser.add_argument('text', type=str, help='Notification text')

    def handle(self, *args, **options):
        username = options['username']
        text = options['text']

        try:
            user = User.objects.get(username=username)
            Notification.objects.create(text=text, user=user, sent=False)
            self.stdout.write(self.style.SUCCESS('Notification created successfully.'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"User '{username}' does not exist."))
