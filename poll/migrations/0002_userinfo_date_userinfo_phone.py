# Generated by Django 4.2.7 on 2023-11-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
