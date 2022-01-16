from django.db import models

# Create your models here.
# core에는 공통적인 것만 들어감(모든 applications에)


class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    created = models.DateTimeField(
        auto_now_add=True, null=True
    )  # 내가 새 model을 생성하게 될때 장고가 현재 날짜랑 시간을 여기에 넣어줌
    updated = models.DateTimeField(
        auto_now=True, null=True
    )  # 매번 내가 Model을 저장할때 마다 항상 장고는 새로운 날짜를 써줌.

    class Meta:  # core파일자체를 데이터베이스에 들어가게 하고 싶지 않기때문에 meta클래스를 만들어줌
        abstract = True  # abstract 모델이지만 데이터베이스에 가지 않은것.
