# Generated by Django 2.1.3 on 2019-03-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190228_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='movieStartTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]