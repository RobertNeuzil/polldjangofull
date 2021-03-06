# Generated by Django 2.1.2 on 2018-10-29 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.TextField(max_length=650)),
                ('reporter', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Partisanlean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partisan', models.BooleanField()),
                ('publication_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Newspaper')),
            ],
        ),
    ]
