# Generated by Django 3.0.8 on 2020-09-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20200922_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='messagei',
        ),
    ]