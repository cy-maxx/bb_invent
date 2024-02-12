# Generated by Django 4.2.10 on 2024-02-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhoisInformation',
            fields=[
                ('domain_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('registrar', models.CharField(blank=True, max_length=255, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('registrant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('registrant_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('nameservers', models.TextField(blank=True, null=True)),
                ('raw_data', models.TextField(blank=True, null=True)),
            ],
        ),
    ]