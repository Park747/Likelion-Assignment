# Generated by Django 4.0.5 on 2022-07-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_visitorlog_likecount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorlog',
            name='likeCount',
        ),
        migrations.AddField(
            model_name='like',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
