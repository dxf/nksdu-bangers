# Generated by Django 3.1.2 on 2020-10-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banger',
            name='certified_show_timestamp',
        ),
    ]