# Generated by Django 4.0.2 on 2022-02-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_contactno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ConnectDate',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
    ]