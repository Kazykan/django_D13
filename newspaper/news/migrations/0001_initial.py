# Generated by Django 4.0.4 on 2022-04-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
    ]
