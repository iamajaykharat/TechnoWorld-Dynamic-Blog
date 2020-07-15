# Generated by Django 3.0.8 on 2020-07-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('msg', models.TextField(verbose_name='Query/Feedback')),
                ('rating', models.CharField(max_length=100, verbose_name='Rating')),
            ],
        ),
    ]