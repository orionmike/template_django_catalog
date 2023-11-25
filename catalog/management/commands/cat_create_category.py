

from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import *

from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        ProductCategory.objects.all().delete()

        # fake = Faker(['ru_RU'])

        cat_name_list = ['Кошельки', 'Сумки', 'Ремни', 'Обложки для документов', 'Кардхолдеры']

        count = 0

        for cat_name in cat_name_list:

            ProductCategory.objects.create(
                title=cat_name,
            )

            count += 1

        print(f'ProductCategory genereited: {count}')
