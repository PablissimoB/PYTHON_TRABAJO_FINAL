# Generated by Django 4.2.2 on 2023-07-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_work_work_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_year',
            field=models.IntegerField(default=2022, max_length=4),
            preserve_default=False,
        ),
    ]
