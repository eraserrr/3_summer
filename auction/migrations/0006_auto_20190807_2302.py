# Generated by Django 2.2.3 on 2019-08-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auto_20190807_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write',
            name='biddings',
            field=models.CharField(default="{u'li':[]}", max_length=200),
        ),
    ]