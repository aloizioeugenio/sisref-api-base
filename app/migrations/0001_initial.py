# Generated by Django 4.1.13 on 2024-05-16 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tabsetor',
            fields=[
                ('codigo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=110, null=True)),
                ('tb0700', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'tabsetor',
                'managed': False,
            },
        ),
    ]
