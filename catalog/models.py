
from django.db import models
from django.urls import reverse
from filebrowser.fields import FileBrowseField
from mptt.models import MPTTModel, TreeForeignKey

from _utils.utils import get_slug


class ProductCategory(MPTTModel):
    title = models.CharField(max_length=150, db_index=True)
    is_publish = models.BooleanField(default=True)
    slug = models.CharField(max_length=150, unique=True)

    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
        verbose_name='Родительская категория')

    image = FileBrowseField(
        "Image", max_length=200, directory="media/practice",
        extensions=[".webp", ".jpg"], blank=True, null=True)

    preview_text = models.TextField(blank=True)
    full_text = models.TextField(blank=True)

    order = models.IntegerField(blank=True, default=100)

    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)
        self.search = f"{self.title}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # def product_list(self):
    #     return Product.objects.filter(category_id=self.pk, is_publish=True)

    def get_url(self):
        return reverse("cat_category_detail", kwargs={"slug": self.slug})

    class MPTTMeta:
        db_table = "catalog_category"
        order_insertion_by = ['title']

    class Meta:
        verbose_name = "Каталог: Категория"
        verbose_name_plural = "Каталог: Категории"


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    is_publish = models.BooleanField(default=True)
    slug = models.CharField(max_length=150, unique=True)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True, default=1)

    image = FileBrowseField(
        "Image", max_length=200, directory="media/work-list",
        extensions=[".webp", ".jpg"], blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)

    preview_text = models.TextField(blank=True, null=True)
    full_text = models.TextField(blank=True, null=True)

    search = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):

        self.slug = get_slug(self.title)
        self.search = f"{self.title}"

        super().save(*args, **kwargs)

    def get_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = "catalog_product"
        ordering = ["title"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
