
from django.core.management.base import BaseCommand
from catalog.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

        print(f'data remove')
