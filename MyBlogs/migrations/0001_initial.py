# Generated by Django 3.2.2 on 2021-05-06 09:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('task', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 5, 6, 9, 36, 16, 685895, tzinfo=utc), verbose_name='Time published')),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
