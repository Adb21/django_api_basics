# Generated by Django 4.0.4 on 2022-05-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('marks', models.IntegerField(max_length=3)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
