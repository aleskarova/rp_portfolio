# Generated by Django 2.2 on 2019-04-06 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descritpion',
            new_name='description',
        ),
    ]
