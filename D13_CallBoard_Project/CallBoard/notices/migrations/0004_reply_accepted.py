# Generated by Django 3.2.2 on 2021-05-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_rename_post_reply_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='accepted',
            field=models.BooleanField(null=True),
        ),
    ]
