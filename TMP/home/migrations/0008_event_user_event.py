# Generated by Django 4.0 on 2022-02-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_event_nop'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user_event',
            field=models.CharField(default='', max_length=122),
        ),
    ]
