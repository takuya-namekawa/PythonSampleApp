# Generated by Django 5.0.4 on 2024-04-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0004_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]