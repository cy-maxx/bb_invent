# Generated by Django 4.2.10 on 2024-02-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('domain', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('site', models.URLField()),
                ('bugbounty', models.URLField()),
            ],
        ),
    ]
