# Generated by Django 2.2.5 on 2020-12-09 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20201208_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bads',
            new_name='beds',
        ),
    ]