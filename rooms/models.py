from asyncio import base_tasks
from ctypes import addressof
from pyexpat import model
from traceback import print_exc
from django.db import models  # 첫번째줄 : 장고 패키지
from django_countries.fields import CountryField  # 두번째 줄: 외부 패키지
from core import models as core_models  # 세번째 줄 : 내 패키지
from users import models as user_models

# Create your models here.

# abstract object for items. many to many
class AbstracctItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# 이클래스를 만든 이유가 roomType을 위해서..


class RoomType(AbstracctItem):
    pass


# 여기서 class abstractitem과 roomtype이 many to many 임.


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
        user_models.User, on_delete=models.CASCADE
    )  # FK one to many
    room_type = models.ManyToManyField(RoomType)  # many to many이기 때문에 foreign키가 아님.

    # 장고와 파이썬은 클래스를 가지고 string으로 만든다. 장고에 있는 모든 클래스 들이 가지고있는 하나의 method가 바로 __str__임
    # 모든 파이썬은 __str__을 가지고 있음.
    def __str__(self):
        return self.name  # 이거를 해줌으로써 이 room에대한 제목을 내가 위에 적은 name 이름으로 바꿔줄 수 가 있음. 그래서
        # 나는 룸 리스트를 이름 순으로 볼 수가 있음. (self.name)
