# Generated by Django 4.2.8 on 2023-12-26 16:37

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_musicitem_image_remove_newsitem_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MusicReleaseTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to='music', verbose_name='image')),
                ('live', models.BooleanField(default=False, verbose_name='live')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='pages.musicrelease')),
            ],
            options={
                'verbose_name': 'music release Translation',
                'db_table': 'pages_musicrelease_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
