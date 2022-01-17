from pyexpat import model
from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(
    admin.ModelAdmin
):  # 이걸 해주면 roomType, facility, amenity, houseRule 이라는(models.py room에 있는거)안에 뭔가를 추가 시켜줄수있음.
    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ "Room Admin Definition"""

    pass


# photo는 다른 어드민에 있기 때문에 이렇게 따로 빼줌.
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """photo admin definition"""

    pass
