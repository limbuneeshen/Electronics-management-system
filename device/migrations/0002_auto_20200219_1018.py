# Generated by Django 3.0.2 on 2020-02-19 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='device/'),
        ),
    ]
