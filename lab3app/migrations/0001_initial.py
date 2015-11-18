# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=30)),
                ('Publisher', models.CharField(max_length=30)),
                ('PublishDate', models.DateField()),
                ('Price', models.IntegerField()),
                ('AuthorID', models.ForeignKey(to='lab3app.Author')),
            ],
        ),
    ]
