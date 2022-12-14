# Generated by Django 4.1 on 2022-08-25 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pin_code', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('grade', models.IntegerField(default=0)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managementSystem.school')),
            ],
        ),
    ]
