# Generated by Django 4.1 on 2022-10-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0042_alter_post_postphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postTags',
            field=models.ManyToManyField(blank=True, to='my_social_app.tag'),
        ),
    ]
