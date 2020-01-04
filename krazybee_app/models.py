from django.db import models


class Album(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Photo(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    thumb_nail_url = models.URLField(max_length=300, null=True, blank=True)
