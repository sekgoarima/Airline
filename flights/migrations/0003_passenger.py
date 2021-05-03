# Generated by Django 3.2 on 2021-05-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210501_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passenger', to='flights.Flight')),
            ],
        ),
    ]
