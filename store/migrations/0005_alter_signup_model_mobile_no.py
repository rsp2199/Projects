# Generated by Django 4.0.6 on 2023-02-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_signup_model_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup_model',
            name='mobile_no',
            field=models.IntegerField(max_length=20),
        ),
    ]