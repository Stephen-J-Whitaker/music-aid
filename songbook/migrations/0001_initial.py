# Generated by Django 3.2.18 on 2023-04-01 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('artist', models.CharField(max_length=150, unique=True)),
                ('lyrics', models.TextField()),
                ('song_slug', models.SlugField(max_length=200, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_songs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='song',
            constraint=models.UniqueConstraint(fields=('title',), name='unique_user_song_title'),
        ),
    ]