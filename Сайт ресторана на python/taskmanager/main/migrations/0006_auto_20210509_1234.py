# Generated by Django 3.1.7 on 2021-05-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_about_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/', verbose_name='Добавьте аватар'),
        ),
    ]
