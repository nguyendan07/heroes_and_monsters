# Generated by Django 2.2.3 on 2019-07-31 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0006_auto_20190731_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('entities.hero',),
        ),
    ]
