# Generated by Django 2.2.4 on 2019-10-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=2, unique=True, verbose_name='小学、中学、高校、大学(修士・博士）'),
        ),
    ]
