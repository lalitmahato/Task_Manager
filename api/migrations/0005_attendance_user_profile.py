# Generated by Django 4.0.4 on 2022-04-20 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.userprofile'),
        ),
    ]