# Generated by Django 3.2 on 2023-07-11 01:45

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default = timezone.now)),
            ],
        ),
    ]
