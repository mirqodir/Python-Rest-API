# Generated by Django 4.0.6 on 2022-07-27 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('UserName', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('CarModel', models.CharField(max_length=100)),
                ('CarNumber', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=100)),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('CreatedUserld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.user')),
            ],
        ),
    ]