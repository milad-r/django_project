# Generated by Django 2.2.7 on 2020-09-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0012_auto_20200728_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/images/profileimages/'),
        ),
    ]
