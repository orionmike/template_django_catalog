
from django.core.management.base import BaseCommand
from faker import Faker
from filebrowser.fields import FileObject
from _generator_image.generate_set import generate_image_category_product

from catalog.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        ProductCategory.objects.all().delete()

        fake = Faker()

        count = 0

        for ind in range(1, 13):

            ind = str(count+1).zfill(2)

            title = f'Category {ind}'
            slug = get_slug(title)

            image_path = f'catalog/category/{slug}/{slug}.webp'

            ProductCategory.objects.create(
                title=title,
                slug=slug,
                image=FileObject(image_path),
                preview_text=fake.paragraph(nb_sentences=2),
                full_text=fake.paragraph(nb_sentences=6),
            )

            generate_image_category_product(image_path)

            count += 1

        print(f'ProductCategory created: {count}')
