
from django.core.management.base import BaseCommand
from faker import Faker
from catalog.models import ProductCategory, Product
from faker.providers import *

import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker(['ru_RU'])

        Product.objects.all().delete()

        cat_list = ProductCategory.objects.all()
        cat_list_id = []

        for c in list(cat_list):
            cat_list_id.append(c.id)

        count = 0

        for index in range(50):

            random_category = random.sample(cat_list_id, 1)

            ind = str(index + 1).zfill(2)
            # image = FileObject(f'catalog/product-{ind}/product-{ind}.webp')

            product = Product.objects.create(
                title=f'Товар {ind}',
                category_id=random_category[0],  # random.randint(40, 50),
                preview_text=fake.paragraph(nb_sentences=2),
                full_text=fake.paragraph(nb_sentences=6),
                price=random.randint(2000, 10000),
                # image=image
            )
            product.save()
            count += 1

        print(f'Product list created: {count}')
