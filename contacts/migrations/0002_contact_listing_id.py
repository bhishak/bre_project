# Generated by Django 2.1.4 on 2018-12-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
