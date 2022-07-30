# Generated by Django 3.2.11 on 2022-07-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CANCELED', 'Canceled'), ('SENT', 'Sent'), ('CREATED', 'Created'), ('PAID', 'Paid'), ('DELIVERED', 'Delivered')], default='CREATED', max_length=16),
        ),
    ]