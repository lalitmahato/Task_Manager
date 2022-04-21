# Generated by Django 4.0.4 on 2022-04-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_username_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, choices=[('Supervisor', 'Supervisor'), ('Intern', 'Intern')], default='Intern', max_length=100, null=True),
        ),
    ]