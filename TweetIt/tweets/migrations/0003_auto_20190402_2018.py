# Generated by Django 2.2 on 2019-04-02 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20190401_1900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-date_posted']},
        ),
    ]
