# Generated by Django 2.1.3 on 2019-02-28 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('actorId', models.AutoField(primary_key=True, serialize=False)),
                ('actorFirstName', models.CharField(max_length=100)),
                ('actorLastName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('directorId', models.AutoField(primary_key=True, serialize=False)),
                ('directorFirstName', models.CharField(max_length=100)),
                ('directorLastName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('genreId', models.AutoField(primary_key=True, serialize=False)),
                ('genreName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MovieActors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.Actors')),
            ],
        ),
        migrations.CreateModel(
            name='MovieDirectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.Directors')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.Genres')),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movieId', models.AutoField(primary_key=True, serialize=False)),
                ('movieName', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('length', models.DurationField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('trailerLink', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='img')),
                ('noRents', models.PositiveIntegerField()),
                ('releaseDate', models.DateField()),
                ('addedDate', models.DateTimeField(auto_now_add=True)),
                ('overallRating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ageRating', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='MovieWriters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writers', to='movies.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Writers',
            fields=[
                ('writerId', models.AutoField(primary_key=True, serialize=False)),
                ('writerFirstName', models.CharField(max_length=100)),
                ('writerLastName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='moviewriters',
            name='writerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.Writers'),
        ),
        migrations.AddField(
            model_name='moviegenres',
            name='movieId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='movies.Movies'),
        ),
        migrations.AddField(
            model_name='moviedirectors',
            name='movieId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directors', to='movies.Movies'),
        ),
        migrations.AddField(
            model_name='movieactors',
            name='movieId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='movies.Movies'),
        ),
        migrations.AlterUniqueTogether(
            name='moviewriters',
            unique_together={('movieId', 'writerId')},
        ),
        migrations.AlterUniqueTogether(
            name='moviegenres',
            unique_together={('movieId', 'genreId')},
        ),
        migrations.AlterUniqueTogether(
            name='moviedirectors',
            unique_together={('movieId', 'directorId')},
        ),
        migrations.AlterUniqueTogether(
            name='movieactors',
            unique_together={('movieId', 'actorId')},
        ),
    ]
