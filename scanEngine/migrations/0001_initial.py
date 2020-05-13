# Generated by Django 3.0.6 on 2020-05-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_type_name', models.CharField(max_length=200)),
                ('subdomain_discovery', models.BooleanField(default=True)),
                ('dir_file_search', models.BooleanField()),
                ('subdomain_takeover', models.BooleanField()),
                ('param_discovery', models.BooleanField()),
                ('port_scan', models.BooleanField()),
            ],
        ),
    ]
