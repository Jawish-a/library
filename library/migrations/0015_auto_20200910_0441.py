# Generated by Django 3.1.1 on 2020-09-10 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_auto_20200910_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='book', to='library.Genre'),
        ),
    ]