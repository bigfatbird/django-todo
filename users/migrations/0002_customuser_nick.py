# Generated by Django 3.0 on 2020-07-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='nick',
            field=models.CharField(default='', max_length=20),
        ),
    ]
