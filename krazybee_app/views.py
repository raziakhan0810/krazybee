import requests
from django.conf import settings
import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from krazybee_app.models import Album, Photo
from krazybee_app.serializers.data import AlbumSerializer, PhotoSerializer

logger = logging.getLogger(__name__)


def get_album_data(item):
    data = AlbumSerializer(item).data
    return data


def get_photo_data(item):
    data = PhotoSerializer(item).data
    return data


class DataInsertAlbumPhoto(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        ALBUM_DATA_INSERT_URL = settings.ALBUM_DATA_INSERT_URL
        PHOTO_DATA_INSERT_URL = settings.PHOTO_DATA_INSERT_URL

        try:
            album_response = requests.get(ALBUM_DATA_INSERT_URL)
            album_data = album_response.json()
            for item in album_data:
                album = Album.objects.create(
                    user_id=item['userId'],
                    title=item['title']
                )
                album.save()

            photo_response = requests.get(PHOTO_DATA_INSERT_URL)
            photo_data = photo_response.json()
            for item in photo_data:
                get_album = Album.objects.get(id=item['albumId'])
                photo = Photo.objects.create(
                    album_id=get_album,
                    title=item['title'],
                    url=item['url'],
                    thumb_nail_url=item['thumbnailUrl']
                )
                photo.save()
            return Response({'success': 'Data inserted successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception('Error while inserting data - {}'.format(e))
            return Response({'message': 'Error while inserting data - {}'.format(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class DataFetchAlbumPhoto(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        get_id = request.query_params.get('id') if 'id' in request.query_params else ''
        get_type = request.query_params.get('type') if 'type' in request.query_params else ''
        get_album = request.query_params.get('album') if 'album' in request.query_params else ''
        datas = []
        try:
            if get_type == 'album':
                album = Album.objects.filter(id=get_id)
                for item in album:
                    data = get_album_data(item)
                    datas.append(data)
                return Response({'data': datas}, status=status.HTTP_200_OK)
            elif get_type == 'photo':
                photo = Photo.objects.filter(id=get_id, album_id=get_album)
                for item in photo:
                    data = get_photo_data(item)
                    datas.append(data)
                return Response({'data': datas}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Data not found!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception('Error while fetching data - {}'.format(e))
            return Response({'message': 'Error while fetching data - {}'.format(e)},
                            status=status.HTTP_400_BAD_REQUEST)
