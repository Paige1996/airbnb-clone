from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):  # 상속 받음. base.py안에있는model으로부터 그리고 AbstracUser로 받았음.
    # abstract모델 이지만 데이터베이스에 가지 않음.
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "EN"),
        (LANGUAGE_KOREAN, "KR"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(
        upload_to="avatar", blank=True
    )  # null은 데이터베이스에 쓰이는 거고 blanks는 form에 적용된느거. 값이 없어도 된다는 뜻.
    # uploads 폴더안의 어떤 폴더에다가 photo를 업로드 할것인지! upload라는 폴더안에 "avatar"라는 파일을 집어넣겠다. 그리고 거기안에 저장하겠다.
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
