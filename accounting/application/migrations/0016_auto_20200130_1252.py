# Generated by Django 3.0 on 2020-01-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_remove_bill_vendor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='items',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='price',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='quantity',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='tax',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bill',
            name='total',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]