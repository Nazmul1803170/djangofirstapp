# Generated by Django 4.0.1 on 2022-08-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='device_linked',
            field=models.BooleanField(default=False),
        ),
    ]
