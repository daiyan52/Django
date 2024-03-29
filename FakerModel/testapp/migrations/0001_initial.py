# Generated by Django 5.0.1 on 2024-01-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll_no', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('dept', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
    ]
