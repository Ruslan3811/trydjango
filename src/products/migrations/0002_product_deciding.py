# Generated by Django 2.0.7 on 2021-08-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Deciding',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
