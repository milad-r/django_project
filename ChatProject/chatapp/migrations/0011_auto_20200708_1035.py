# Generated by Django 2.2.7 on 2020-07-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0010_auto_20200218_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reg_google',
            field=models.CharField(max_length=400, null=True),
        ),
    ]