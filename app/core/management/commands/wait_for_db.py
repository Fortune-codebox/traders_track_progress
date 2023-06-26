"""
Django command to wait for db to be available
"""
import time

from django.db.utils import DatabaseError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
      Django command to wait for db
    """

    def handle(self, *args, **options):
        """Entrypoint for Command"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (DatabaseError):
                self.stdout.write('Database Unavailable waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available!'))
