# Generated by Django 3.2.4 on 2021-06-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0010_auto_20210617_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='photo',
            field=models.ImageField(default='', upload_to='profile'),
            preserve_default=False,
        ),
    ]
