# Generated by Django 5.0.4 on 2024-04-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]