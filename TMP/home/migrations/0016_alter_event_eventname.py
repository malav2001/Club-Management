# Generated by Django 4.0 on 2022-03-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventname',
            field=models.CharField(default='', max_length=122, null=True),
        ),
    ]
