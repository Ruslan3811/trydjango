# Generated by Django 2.0.7 on 2021-08-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210828_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=10000),
        ),
    ]
