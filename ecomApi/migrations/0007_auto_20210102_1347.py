# Generated by Django 3.1.3 on 2021-01-02 07:47

from django.db import migrations, models
import ecomApi.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApi', '0006_orders_placement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.CharField(default=ecomApi.models.random_string, max_length=6, primary_key=True, serialize=False),
        ),
    ]