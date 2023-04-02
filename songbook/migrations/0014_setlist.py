# Generated by Django 3.2.18 on 2023-04-02 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songbook', '0013_auto_20230402_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setlist_name', models.CharField(max_length=150)),
                ('songs_in_setlist', models.ManyToManyField(related_name='songs_in_setlist', to='songbook.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setlist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
