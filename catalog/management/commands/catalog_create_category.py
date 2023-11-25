
from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import *

from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        ProductCategory.objects.all().delete()

        fake = Faker()

        count = 0

        for _ in range(10):

            ind = str(count+1).zfill(2)

            ProductCategory.objects.create(
                title=f'Category-{ind}'
            )

            count += 1

        print(f'ProductCategory created: {count}')
