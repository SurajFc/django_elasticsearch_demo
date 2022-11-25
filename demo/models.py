from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            null=False, blank=False)
    email = models.EmailField('email address')


class Movie(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            null=False, blank=False)
    artist = models.ForeignKey(Artist, null=True,
                               blank=False, on_delete=models.CASCADE, related_name="artist")
    description = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
