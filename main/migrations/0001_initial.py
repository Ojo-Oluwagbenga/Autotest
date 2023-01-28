# Generated by Django 4.1 on 2023-01-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('creatorid', models.CharField(max_length=20)),
                ('classid', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('deadline', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemcode', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('matric', models.CharField(max_length=20)),
                ('cashbalance', models.FloatField()),
                ('accept_status', models.CharField(default=0, max_length=20)),
                ('user_type', models.CharField(max_length=20)),
            ],
        ),
    ]
