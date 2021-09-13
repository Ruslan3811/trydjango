# Generated by Django 2.0.7 on 2021-08-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210827_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
