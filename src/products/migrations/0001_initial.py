# Generated by Django 2.0.7 on 2021-08-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('summary', models.TextField()),
            ],
        ),
    ]
