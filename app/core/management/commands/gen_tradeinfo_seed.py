"""
Django command to wait for db to be available
"""
import datetime
import time
import json
from django.core.management.base import BaseCommand
from core.models import TradeInfo
from django.core.files import File
from django.contrib.auth import get_user_model
import random


class Command(BaseCommand):
    """
      Django command to wait for db
    """

    def handle(self, *args, **options):
        """Entry"""
        # with open('/app/core/management/commands/tradeinfo.json') as f:
        #     file_contents = File(f)
        #     file_contents = file_contents.read()

        # parsed_tradeinfo = json.loads(file_contents)
        # User = get_user_model().objects
        # users = User.values()
        # tradeinfo_2 = TradeInfo.objects.filter(user_id=4).values()
        cur_user = get_user_model().objects.filter(id=2).values()

        # d = []
        # for _ in range(len(tradeinfo_2)):
        #     d.append(tradeinfo_2[_]['profit'])

        # for _ in range(2, 12):
        #     cur_user = users.get(id=_)

        #     # del cur_user['id']
        #     # del cur_user['is_active']
        #     # del cur_user['is_staff']
        #     # del cur_user['is_superuser']
        #     # del cur_user['last_login']
        #     # del cur_user['password']

        #     for i in parsed_tradeinfo:
        #         profit = random.randint(-100, 101)
        #         balance = cur_user['account_balance'] + (profit)

        #         if balance >= 0:
        #             cur_user.update({'account_balance': balance})
        #             User.update_or_create(
        #                 email=cur_user['email'],
        #                 name=cur_user['name'],
        #                 defaults={
        #                     'account_balance': cur_user['account_balance'],
        #                     'name': cur_user['name']
        #                 })

        #             TradeInfo.objects.create(
        #                 user_id=cur_user['id'],
        #                 profit=profit,
        #                 balance=balance,
        #                 market=i['market'],
        #                 time_date=datetime.datetime.now()
        #             )

        #         else:
        #             continue

        # self.stdout.write(self.style.SUCCESS('Successful!!!'))
        self.stdout.write(self.style.SUCCESS(cur_user[0]))
