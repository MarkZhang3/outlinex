# Generated by Django 3.2.4 on 2022-08-20 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outline', '0004_remove_user_app_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='AppPassword',
        ),
    ]
