# Generated by Django 5.0.7 on 2024-11-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=20),
        ),
    ]