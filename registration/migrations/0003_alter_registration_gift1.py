# Generated by Django 5.2.3 on 2025-07-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gift1',
            field=models.URLField(default='none'),
            preserve_default=False,
        ),
    ]
