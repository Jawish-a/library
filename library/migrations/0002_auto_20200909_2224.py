# Generated by Django 3.1.1 on 2020-09-09 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mempership', to='library.membership'),
        ),
    ]