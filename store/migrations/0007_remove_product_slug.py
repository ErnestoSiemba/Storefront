# Generated by Django 4.0.6 on 2022-07-29 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_collection_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
