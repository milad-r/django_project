# Generated by Django 2.2.7 on 2020-02-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_auto_20200208_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='0', max_length=11, unique=True),
        ),
    ]
