from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.RoomType)
class ItemAdmin(
    admin.ModelAdmin
):  # 이걸 해주면 roomType이라는(models.py room에 있는거)안에 뭔가를 추가 시켜줄수있음.
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass
