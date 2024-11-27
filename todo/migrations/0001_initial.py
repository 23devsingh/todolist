# Generated by Django 5.0.1 on 2024-10-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=400)),
                ('is_complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
