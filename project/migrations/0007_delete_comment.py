# Generated by Django 3.2.7 on 2021-09-15 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_delete_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
