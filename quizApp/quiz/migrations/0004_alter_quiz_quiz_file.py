# Generated by Django 5.0 on 2023-12-07 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
