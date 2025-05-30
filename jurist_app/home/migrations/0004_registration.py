# Generated by Django 5.0.3 on 2024-03-12 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=255)),
                ('l_phone', models.CharField(max_length=10)),
                ('l_email', models.EmailField(max_length=254)),
                ('l_location', models.CharField(max_length=255)),
                ('l_education', models.TextField()),
                ('l_address', models.TextField()),
                ('law_exp', models.IntegerField()),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
    ]
