# Generated by Django 2.2.4 on 2019-10-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0008_wordhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
