# Generated by Django 4.2.11 on 2024-04-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='aleatorio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]