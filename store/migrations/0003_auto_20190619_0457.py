# Generated by Django 2.2.1 on 2019-06-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190607_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='book',
            name='total_user',
            field=models.IntegerField(default=0),
        ),
    ]