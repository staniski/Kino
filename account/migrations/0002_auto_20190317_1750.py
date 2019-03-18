# Generated by Django 2.1.3 on 2019-03-17 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoviestats',
            name='lastWatchPos',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='usermoviestats',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moviestats', to=settings.AUTH_USER_MODEL),
        ),
    ]
