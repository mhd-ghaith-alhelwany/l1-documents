# Generated by Django 3.1.3 on 2020-11-27 23:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 11, 27, 23, 8, 48, 261486))),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('json', models.CharField(max_length=5000)),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.document')),
            ],
        ),
    ]