# Generated by Django 5.2.4 on 2025-07-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_alter_user_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.CharField(max_length=72),
        ),
    ]
