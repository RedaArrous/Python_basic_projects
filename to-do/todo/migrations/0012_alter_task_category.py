# Generated by Django 5.1.7 on 2025-03-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
