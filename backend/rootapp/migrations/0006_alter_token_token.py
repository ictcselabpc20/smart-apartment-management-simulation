# Generated by Django 4.2.4 on 2023-10-16 08:12

from django.db import migrations, models
import rootapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0005_alter_record_who_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='12666686E757', max_length=12, unique=True, validators=[rootapp.validators.token_validator]),
        ),
    ]