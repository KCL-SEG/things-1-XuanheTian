# Generated by Django 4.2.5 on 2023-10-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_alter_thing_description_alter_thing_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
