# Generated by Django 3.2.5 on 2022-01-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos/%Y/%m/%d/'),
        ),
    ]