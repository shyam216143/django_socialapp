# Generated by Django 4.1 on 2022-08-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social_Media_App', '0004_posting'),
    ]

    operations = [
        migrations.CreateModel(
            name='likepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
