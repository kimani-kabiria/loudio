from django.db import models


class Station(models.Model):
    st_name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    st_tagline = models.CharField(max_length=250)
    st_bio = models.CharField(max_length=1000)
    st_icon = models.FileField()
    st_freq = models.CharField(max_length=100)
    st_live_link = models.CharField(max_length=1000)
