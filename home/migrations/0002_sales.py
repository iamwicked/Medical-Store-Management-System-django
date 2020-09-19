# Generated by Django 3.0.8 on 2020-09-19 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_json', models.CharField(max_length=900)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
