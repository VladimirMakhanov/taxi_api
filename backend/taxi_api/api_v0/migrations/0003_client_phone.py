# Generated by Django 2.0.3 on 2018-03-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0002_order_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='', max_length=19),
        ),
    ]
