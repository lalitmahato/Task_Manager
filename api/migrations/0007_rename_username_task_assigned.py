# Generated by Django 4.0.4 on 2022-04-20 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_user_profile_attendance_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='username',
            new_name='assigned',
        ),
    ]
