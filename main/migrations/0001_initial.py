# Generated by Django 3.2.9 on 2021-11-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=125, verbose_name='Why')),
                ('basis', models.TextField(max_length=10000, verbose_name='Description')),
            ],
        ),
    ]
