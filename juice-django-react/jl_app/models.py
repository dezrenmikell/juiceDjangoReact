from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=400)
    description = models.CharField(max_length=800)

    def __str__(self):
        return self.name

class Poem(models.Model):
    title = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=400)
    preview_url = models.CharField(max_length=400)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='poems')

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    preview_url = models.CharField(max_length=800)

    def __str__(self):
        return self.title

class Picture(models.Model):
    title = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title