# Generated by Django 2.2 on 2020-01-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', null=True)),
                ('longitude', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('latitude', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('category', models.CharField(blank=True, default=0, max_length=2, null=True)),
            ],
        ),
    ]
