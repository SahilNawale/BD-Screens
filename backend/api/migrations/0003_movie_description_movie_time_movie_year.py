# Generated by Django 4.1.1 on 2022-09-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_upcomingmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='time',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
