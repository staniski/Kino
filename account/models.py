from django.db import models
from django.contrib.auth.models import User as Auth_User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie, Genre


class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(Auth_User, on_delete=models.CASCADE)
    completedTutorial = models.BooleanField(default=False)
    dob = models.DateField(auto_now_add=True)
    profilePic = models.ImageField(upload_to='profile_img', blank=True)

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#    instance.profile.save()


class UserMovieStats(models.Model):
    userId = models.ForeignKey(Auth_User, related_name='moviestats', on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movie, related_name='userstats', on_delete=models.CASCADE)
    rating = models.IntegerField(default=None, validators=[MaxValueValidator(5), MinValueValidator(1)], blank=True, null=True)
    lastWatchPos = models.DurationField(blank=True, null=True)
    recommendValue = models.DecimalField(decimal_places=2, max_digits=4, default=None,validators=[MaxValueValidator(5),MinValueValidator(0)], blank=True, null=True)
    allowRecommend = models.BooleanField(default=True)
    lastRating = models.DateTimeField(auto_now_add=True,null=True,blank=True)

class FavouriteGenres(models.Model):
    userId = models.ForeignKey(Auth_User, related_name='favouritegenres', on_delete=models.CASCADE)
    genreId = models.ForeignKey(Genre, related_name='usersfavourite', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('userId', 'genreId')

#class rentalTimer(models.Model):
    #rentalID = models.AutoField(primary_key=True)
    #movieID = models.ForeignKey(related_name='movie', on_delete=models.CASCADE)
    #userId = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    #rentTime = orderCreated = models.DateTimeField(auto_now_add=True)
