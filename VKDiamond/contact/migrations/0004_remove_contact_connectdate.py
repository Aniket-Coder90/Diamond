# Generated by Django 4.0.2 on 2022-02-25 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_connectdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='ConnectDate',
        ),
    ]
