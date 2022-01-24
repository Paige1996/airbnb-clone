from encodings import search_function
from itertools import product
from operator import mod
from pyexpat import model
from django.contrib import admin
from django.utils.html import mark_safe

# 실제 사진을 클릭하지 않고 바로 보여주기 위해 html을 여기다 임의로 추가하는데 추가할때 적어줘야함
from . import models


# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(
    admin.ModelAdmin
):  # 이걸 해주면 roomType, facility, amenity, houseRule 이라는(models.py room에 있는거)안에 뭔가를 추가 시켜줄수있음.
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):  # 룸 안 사진을 목록들을 넣는 방식

    model = models.Photo


# inline modelAdmin


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (
        PhotoInline,
    )  # 룸 안에 사진 목록들을 넣는 방식. 클래스 photo 에 FK가 room이 돼 있으므로 이렇게 만 설정
    # 필드 셋은 예쁘께 꾸며주기 위해~!
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "baths")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "More about space",
            {
                "classes": ("collapse",),  # 이건 접을 수 있는 섹션을 만들어 줌
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        (
            "Last details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price")  # 어드민 패널에 이름이나 가격 순으로 ordering할 수 있는 것.

    list_filter = ("instant_book", "city", "country")  # 옆꿀떼기에 필터 박스가 생성됨

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    # city 마다 서치 할 수 있음. ^이거는 뭐냐면 원래는 장고가 city에 soul중에 oul적어도 그냥 서치 할 수 있는데 ^를 하면 딱 내가
    # 검색 한 것만 딱 할 수 있게 만듬. 그리고 반드시 ()안에 하나만 들어있다면 꼭 ,가 마지막으로 적혀야 오류가 안남
    # city로 검색했는데도 불구하고 나오지 않으면 username으로 검색할수있게 하는데 그게 room에서는 foreign키고 그거는 host__username으로 됨
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields

    raw_id_fields = ("host",)  # 디테일에 host이름을 클릭하고 나면 번호로 지정되게 함. 그리고

    search_fields = ("^city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    # 어드민 페널에 들어가면 저 세개는 뭔가 어드민이 필터할 수있는 박스나등등을 만들어 줄 수있음. only many to many만 가능할두ㅡㅅ?
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

    # 위에서 적은것 처럼 그냥 나열도 되지만 내 마음대로 이름을 커스터마이징 할 수 가 있는데,
    # 그때 함수를 쓴다. ameninties의 갯수를 새아리기 위해 적을 수 있는 것은?
    def count_amenities(self, obj):
        return obj.amenities.count()

    # count_amenities.short_description = "hello!" 칼럼이름을 새로 쓸수있음

    def count_photos(self, obj):
        return obj.photos.count()


# admin에 있는 함수는 두가지를 가지는데 하나는 self는 RoomAdmin 클래스이고, obj는 현재 row이다.


# photo는 다른 어드민에 있기 때문에 이렇게 따로 빼줌.
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """photo admin definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    # 실제 사진을 클릭하지 않고 바로 보여주기 위해 사진 주사 + html을 여기다 임의로 추가하는데 추가할때 mark_safe를 앞에 적어줘야함

    get_thumbnail.short_description = "Thumbnail"
