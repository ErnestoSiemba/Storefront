# Generated by Django 4.0.6 on 2022-07-27 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_customer_table'),
    ]

    operations = [
        migrations.RunSQL("""
                          INSERT INTO store_collection (title)
                          VALUES ('collection1')
                          """, """
                          DELETE FROM store_collection WHERE title = 'collection1'
                          """)

    ]