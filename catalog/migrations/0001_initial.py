# Generated by Django 4.2.6 on 2023-11-25 16:57

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_publish', models.BooleanField(default=True)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image')),
                ('preview_text', models.TextField(blank=True)),
                ('full_text', models.TextField(blank=True)),
                ('order', models.IntegerField(blank=True, default=100)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.productcategory', verbose_name='Родительская категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('is_publish', models.BooleanField(default=True)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('preview_text', models.TextField(blank=True, null=True)),
                ('full_text', models.TextField(blank=True, null=True)),
                ('search', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.productcategory')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'catalog_product',
                'ordering': ['title'],
            },
        ),
    ]