# Generated by Django 2.0 on 2019-05-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190502_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_first_name', models.CharField(max_length=20)),
                ('user_last_name', models.CharField(max_length=20)),
            ],
        ),
    ]
