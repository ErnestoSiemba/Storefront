# Generated by Django 4.1.1 on 2022-09-13 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_customer_birth_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
