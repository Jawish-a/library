# Generated by Django 3.1.1 on 2020-09-09 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20200910_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
