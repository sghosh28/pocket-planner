# Generated by Django 4.0.3 on 2022-05-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_schema_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='domain_url',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
