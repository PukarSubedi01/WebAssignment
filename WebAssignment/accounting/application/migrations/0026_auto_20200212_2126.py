# Generated by Django 3.0 on 2020-02-12 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0025_auto_20200212_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='billDate',
            new_name='bill_date',
        ),
    ]