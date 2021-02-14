# Generated by Django 3.1.4 on 2021-02-13 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('send_client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]