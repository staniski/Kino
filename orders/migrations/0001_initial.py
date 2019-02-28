# Generated by Django 2.1.5 on 2019-02-28 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('paid', models.BooleanField(default=False)),
                ('card_number', models.CharField(max_length=16)),
                ('cardholder_name', models.CharField(max_length=200)),
                ('expiry_date', models.CharField(max_length=7)),
                ('CVV_code', models.CharField(max_length=3)),
                ('orderCreated', models.DateTimeField(auto_now_add=True)),
                ('orderUpdated', models.DateTimeField(auto_now=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='account.User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('movieStartTime', models.DateTimeField(blank=True)),
                ('movieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='movies.Movie')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='orders.Order')),
            ],
        ),
    ]
