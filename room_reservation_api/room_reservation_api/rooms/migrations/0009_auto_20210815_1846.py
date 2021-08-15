# Generated by Django 3.2.6 on 2021-08-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20210815_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='external_visitor',
            field=models.ManyToManyField(to='rooms.ExternalVisitor', verbose_name='Add external visitors data'),
        ),
    ]
