# Generated by Django 3.2.11 on 2022-06-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='prosuct',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CANCELED', 'Canceled'), ('PAID', 'Paid'), ('SENT', 'Sent'), ('DELIVERED', 'Delivered'), ('CREATED', 'Created')], default='CREATED', max_length=16),
        ),
    ]
