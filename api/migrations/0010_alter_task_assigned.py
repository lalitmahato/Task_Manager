# Generated by Django 4.0.4 on 2022-04-21 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile'),
        ),
    ]