# Generated by Django 3.2.2 on 2021-05-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_alter_visitor_last_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='last_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
