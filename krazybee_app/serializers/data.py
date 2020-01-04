from rest_framework import serializers

from krazybee_app.models import Album, Photo


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'user_id', 'title')


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'album_id', 'title', 'url', 'thumb_nail_url')
