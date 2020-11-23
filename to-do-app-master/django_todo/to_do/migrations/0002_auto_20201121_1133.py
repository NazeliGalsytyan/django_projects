# Generated by Django 3.1.3 on 2020-11-21 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtask',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newtask',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Doing'), (2, 'Done')], default=0),
        ),
    ]