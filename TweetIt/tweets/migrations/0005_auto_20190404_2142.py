# Generated by Django 2.2 on 2019-04-04 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20190402_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-date_posted']},
        ),
    ]
