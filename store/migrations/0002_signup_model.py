# Generated by Django 4.0.6 on 2023-02-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('mobile_no', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('cnfpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
