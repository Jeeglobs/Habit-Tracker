# Generated by Django 4.1.7 on 2023-03-19 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_record_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]