# Generated by Django 2.2.5 on 2020-12-09 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20201209_0631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='amenties',
            new_name='amenities',
        ),
    ]
