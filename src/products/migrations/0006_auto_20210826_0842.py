# Generated by Django 2.0.7 on 2021-08-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210821_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Deciding',
            field=models.BooleanField(default=False),
        ),
    ]
