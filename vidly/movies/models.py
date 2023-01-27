from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharFeild(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatFeild()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

