# Generated by Django 3.2.2 on 2021-05-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_alter_visitor_last_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='registration_mail_sent',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
