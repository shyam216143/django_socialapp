# Generated by Django 4.0.7 on 2022-10-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_social_app', '0011_alter_countries_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.DeleteModel(
            name='Countries',
        ),
    ]