# Generated by Django 4.1 on 2022-09-13 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Social_Media_App', '0008_groups_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('first_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thread1', to=settings.AUTH_USER_MODEL)),
                ('second_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thread2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('first_person', 'second_person')},
            },
        ),
        migrations.CreateModel(
            name='Messages1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('thread', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message1', to='Social_Media_App.threadingtable')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
