# Generated by Django 4.1.1 on 2022-09-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
