# Generated by Django 3.1.3 on 2020-12-05 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201205_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user_type',
        ),
    ]
