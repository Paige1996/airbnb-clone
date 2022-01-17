from asyncio import base_tasks
from ctypes import addressof
from pyexpat import model
from traceback import print_exc
from django.db import models  # 첫번째줄 : 장고 패키지
from django_countries.fields import CountryField  # 두번째 줄: 외부 패키지
from core import models as core_models  # 세번째 줄 : 내 패키지


# Create your models here.


class AbstracctItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# 이클래스를 만든 이유가 roomType을 위해서..


class RoomType(AbstracctItem):

    """RoomType Object Definition"""

    class Meta:
        verbose_name = "Room Type"

    # class meta안에 다른 것들도 많은데, 예를들면 orderign!  ordering = ['-created']이런식으로 하면 생성된 순서부터 정렬될수도있고...
    # 마이너스는 거꾸로, 마이너스가 없으면 순서대로 ordering = ["name"] 알파뱃 순도 가능


# 초반에 생성될때 장고는 뒤에 s를 붙인다. 내 마음대로 이름을 넣어주기 위해 좀 고치자면
class Amenity(AbstracctItem):
    """Amenity Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"  # 장고가 자동으로 Amenitys이러헤 된것을 verbose_name_plural로 s를 Amenities로 예쁘게


class Facility(AbstracctItem):
    """Facility model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstracctItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"  # 장고가 자동으로 House rulse이러헤 된것을 verbose_name로 대문자 R을 해주고 뒤에s는 안붙이고!(자동으로 붙여질거니까)


class Photo(core_models.TimeStampedModel):
    """photo model definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(
        "Room", on_delete=models.CASCADE
    )  # room을 지우면 자동으로 자동으로 사진도 지워지니까 CASCADE

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User",  # user는 users안에 있으니까
        on_delete=models.CASCADE,  # 여기서 on_delete은 만약 여기서 foreign키인 user가 삭제 되었다면 전체 룸을 삭제해야함
    )  # one to many를 쓰는 자는 Foreign key!!
    room_type = models.ForeignKey(
        "RoomType", on_delete=models.SET_NULL, null=True
    )  # 하나의 방에선 하나혹은 둘의 룸타입만 존재하기때문에 one to many 라서 forekey.
    # 근데 룸이 여러개가 있고 룸타입이 여러개가 있다?이럴땐 manytomanyfield를 써야함.  여기서 on_delete이 models.Set_null인데 장고 도큐먼트를 보면 그건
    # 위에와 다르게 roomType이 삭제 되어도 괜찮음. 대신 models.Set_null을 쓸때 null=True도 함께 써준다
    # https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html 참조

    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    # 장고와 파이썬은 클래스를 가지고 string으로 만든다. 장고에 있는 모든 클래스 들이 가지고있는 하나의 method가 바로 __str__임
    # 모든 파이썬은 __str__을 가지고 있음.
    def __str__(self):
        return self.name  # 이거를 해줌으로써 이 room에대한 제목을 내가 위에 적은 name 이름으로 바꿔줄 수 가 있음. 그래서
        # 나는 룸 리스트를 이름 순으로 볼 수가 있음. (self.name)
