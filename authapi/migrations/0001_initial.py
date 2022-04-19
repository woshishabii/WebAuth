# Generated by Django 4.0.3 on 2022-04-09 04:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.UUID('b2e86b97-dba2-4167-a89c-31a33c60574b'), editable=False, primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=50)),
                ('force', models.BooleanField()),
                ('views', models.IntegerField(default=0)),
                ('link', models.TextField(blank=True)),
                ('announcement', models.TextField(blank=True)),
                ('update', models.TextField(blank=True)),
                ('md5', models.CharField(blank=True, max_length=32)),
            ],
        ),
    ]