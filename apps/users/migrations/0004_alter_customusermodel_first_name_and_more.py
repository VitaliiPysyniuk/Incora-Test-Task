# Generated by Django 4.1.2 on 2022-10-10 19:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customusermodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='first_name',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(message='The first name can contain only latin letters.', regex='^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=60, validators=[django.core.validators.RegexValidator(message='The last name can contain only latin letters.', regex='^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='phone',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid phone number format.', regex='^\\+?(38)?\\(?0[1-9]{2}\\)?[0-9]{2}-?[0-9]{3}-?[0-9]{2}$')]),
        ),
    ]