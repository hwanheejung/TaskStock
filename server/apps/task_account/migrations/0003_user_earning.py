# Generated by Django 3.2 on 2023-08-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_account', '0002_auto_20230819_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='earning',
            field=models.IntegerField(default=0),
        ),
    ]