# Generated by Django 4.2.3 on 2024-01-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_needed_by_project_pet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='anonymous',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
