# Generated by Django 2.2.3 on 2019-07-31 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0005_auto_20190731_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='added_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='villain',
            name='added_on',
            field=models.DateField(auto_now=True),
        ),
    ]
