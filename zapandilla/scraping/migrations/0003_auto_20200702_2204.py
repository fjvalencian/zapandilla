# Generated by Django 3.0.8 on 2020-07-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20200702_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapatilla',
            name='currrent_price',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='zapatilla',
            name='price',
            field=models.CharField(max_length=250),
        ),
    ]