# Generated by Django 5.1.1 on 2024-10-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_ad_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='condition',
            field=models.CharField(default='yaxshi', max_length=150),
            preserve_default=False,
        ),
    ]
