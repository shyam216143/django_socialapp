# Generated by Django 4.0.7 on 2022-10-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0037_rename_date_created_tag_datecreated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='commentCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='shareCount',
            field=models.IntegerField(default=0),
        ),
    ]
