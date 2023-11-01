# Generated by Django 4.2.4 on 2023-10-16 18:49

from django.db import migrations, models
import rootapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rootapp', '0006_alter_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='126666887C46', max_length=12, unique=True, validators=[rootapp.validators.token_validator]),
        ),
    ]