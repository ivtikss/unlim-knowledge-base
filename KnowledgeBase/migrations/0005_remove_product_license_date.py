# Generated by Django 4.2.2 on 2023-11-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0004_product_contact_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='license_date',
        ),
    ]
