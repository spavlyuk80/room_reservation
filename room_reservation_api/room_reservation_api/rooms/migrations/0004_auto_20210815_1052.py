# Generated by Django 3.2.6 on 2021-08-15 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0003_alter_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='reservation_author', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rooms.room'),
        ),
    ]
