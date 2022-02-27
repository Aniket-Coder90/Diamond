# Generated by Django 4.0.2 on 2022-02-25 13:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ConnectDate', models.DateTimeField(auto_created=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('ContactNo', models.IntegerField(max_length=15)),
                ('TextMessage', models.TextField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]