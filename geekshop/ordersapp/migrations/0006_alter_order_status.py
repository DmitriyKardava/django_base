# Generated by Django 3.2.11 on 2022-07-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('DELIVERED', 'Delivered'), ('SENT', 'Sent'), ('CREATED', 'Created'), ('PAID', 'Paid'), ('CANCELED', 'Canceled')], default='CREATED', max_length=16),
        ),
    ]
