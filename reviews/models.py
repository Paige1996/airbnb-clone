from tkinter import CASCADE
from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """Review model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )  # user가 삭제되면 리뷰가 삭제돼야함
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"
        # 결과는... 리뷰이름  - room 이름이 나타날 것임.  왜 self.room.name을 하지 않았냐면, room의 models.py에 __str__이 self.name 이있음

    # return  self.room.host.username
    # -> 이거는... room 안에 host. host안에 user. user은 AbstractUser이 상속받은거... 결국 AbstractUser안에 username

    # 하나의 리뷰에 대한 평균을 내고싶음...
    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "AVG."
