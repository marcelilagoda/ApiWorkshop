# Generated by Django 3.0.3 on 2020-02-27 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('director', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('genre', models.CharField(choices=[(1, 'Action'), (2, 'Comedy'), (3, 'Crime'), (4, 'Independent'), (5, 'Documentary'), (6, 'Drama'), (7, 'War')], max_length=21)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_books.Book')),
            ],
        ),
    ]
