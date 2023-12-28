# Generated by Django 4.2.8 on 2023-12-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetranslation',
            name='page_type',
            field=models.CharField(choices=[('home', 'Home'), ('band', 'Band'), ('music', 'Music'), ('tour', 'Tour'), ('news', 'News'), ('shop', 'Shop')], default='home', max_length=5, verbose_name='page type'),
        ),
    ]