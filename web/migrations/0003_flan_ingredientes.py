# Generated by Django 3.2.4 on 2022-03-28 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='ingredientes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
