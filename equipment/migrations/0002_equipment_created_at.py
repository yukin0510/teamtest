# Generated by Django 4.2.10 on 2024-08-04 17:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]