# Generated by Django 3.2.6 on 2021-08-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20210815_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('R', 'RESERVED'), ('C', 'CANCELLED')], default='R', max_length=1),
        ),
    ]
