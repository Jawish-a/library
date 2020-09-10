# Generated by Django 3.1.1 on 2020-09-09 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0010_auto_20200910_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='manager',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='library', to=settings.AUTH_USER_MODEL),
        ),
    ]