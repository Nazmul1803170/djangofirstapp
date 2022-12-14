# Generated by Django 4.0.1 on 2022-08-15 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='manufacturer',
            field=models.CharField(default='ShantoTech Ltd', max_length=50),
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('payment', models.CharField(max_length=20)),
                ('order_receive', models.BooleanField()),
                ('order_delevary', models.BooleanField()),
                ('order_delevered', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
