# Generated by Django 4.2.3 on 2024-01-27 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_img',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_desc',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]