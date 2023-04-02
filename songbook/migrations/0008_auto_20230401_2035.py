# Generated by Django 3.2.18 on 2023-04-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0007_alter_song_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AddConstraint(
            model_name='song',
            constraint=models.UniqueConstraint(fields=('user', 'title'), name='unique_user_song_title'),
        ),
    ]