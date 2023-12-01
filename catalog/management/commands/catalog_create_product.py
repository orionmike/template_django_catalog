
import random

from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import *
from filebrowser.fields import FileObject

from _generator_image.generate_set import generate_image_product
from catalog.models import Product, ProductCategory


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker(['ru_RU'])

        Product.objects.all().delete()

        cat_list = ProductCategory.objects.all()

        count = 0

        for index in range(100):

            random_category = random.choice(cat_list)

            ind = str(index + 1).zfill(2)

            image_path = f'catalog/product/{random_category.slug}/product-{ind}/product-{ind}.webp'
            generate_image_product(image_path)

            product = Product.objects.create(
                title=f'Product {ind}',
                category_id=random_category.id,
                preview_text=fake.paragraph(nb_sentences=2),
                full_text=fake.paragraph(nb_sentences=6),
                price=random.randint(2000, 10000),
                image=FileObject(image_path),
            )
            product.save()

            count += 1

        print(f'Product list created: {count}')
