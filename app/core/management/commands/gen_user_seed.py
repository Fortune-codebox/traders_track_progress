"""
Django command to wait for db to be available
"""
import time
import json
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files import File


class Command(BaseCommand):
    """
      Django command to wait for db
    """

    def handle(self, *args, **options):
        """Entrypoint for Command"""
        with open('/app/core/management/commands/users.json') as f:
            file_contents = File(f)
            file_contents = file_contents.read()

        parsed_users = json.loads(file_contents)

        for _ in parsed_users:
            get_user_model().objects.create_user(
                email=_['email'],
                password=_['password'],
                name=_['name'],
                account_balance=_['account_balance']
            )

        self.stdout.write(self.style.SUCCESS(
            'User Data Created Successfully!'))
