from django.contrib import admin

from krazybee_app.models import Album, Photo


@admin.register(Album)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title')


@admin.register(Photo)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_id', 'title', 'url', 'thumb_nail_url')
