# Generated by Django 3.1.1 on 2020-09-09 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20200910_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genre',
            new_name='genres',
        ),
    ]
