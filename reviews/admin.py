from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    pass

    # 한 리뷰의 평균을 얻는 것
    list_display = (
        "__str__",
        "rating_average",
    )  # __str__? return된 내 방 이름, rating average 함수를 보여줌.
