# Generated by Django 4.0.7 on 2022-10-14 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0028_alter_post_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 0, 1, 3, 20123)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_last_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 0, 1, 3, 20123)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_photo',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_tag',
        ),
        migrations.AddField(
            model_name='post',
            name='post_tag',
            field=models.ManyToManyField(blank=True, null=True, to='my_social_app.tag'),
        ),
    ]
