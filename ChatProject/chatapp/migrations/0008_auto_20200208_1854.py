# Generated by Django 2.2.7 on 2020-02-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0007_auto_20200208_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profileimages'),
        ),
    ]
