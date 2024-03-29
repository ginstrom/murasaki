# Generated by Django 4.2.8 on 2023-12-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_musicitem_newsitem_tourdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdatetranslation',
            name='title',
            field=models.CharField(default='title', max_length=300, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tourdatetranslation',
            name='location',
            field=models.CharField(blank=True, max_length=300, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='tourdatetranslation',
            name='venue',
            field=models.CharField(blank=True, max_length=300, verbose_name='venue'),
        ),
    ]
