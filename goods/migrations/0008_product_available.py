# Generated by Django 4.2 on 2024-04-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_alter_product_options_product_article_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
