# Generated by Django 4.0.4 on 2022-05-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_visitorlog_numberview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorlog',
            name='numberView',
            field=models.CharField(default=0, max_length=100),
        ),
    ]