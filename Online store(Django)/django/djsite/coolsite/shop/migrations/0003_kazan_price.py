# Generated by Django 4.0.6 on 2022-08-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_kazan_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='kazan',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
