# Generated by Django 4.2.7 on 2024-05-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default='none', max_length=1000),
            preserve_default=False,
        ),
    ]
