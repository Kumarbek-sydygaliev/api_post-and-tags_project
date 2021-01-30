# Generated by Django 3.1.4 on 2021-01-26 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmcode',
            name='reset',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='confirmcode',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to=settings.AUTH_USER_MODEL),
        ),
    ]
