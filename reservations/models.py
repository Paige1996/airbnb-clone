from email.policy import default
from django.db import models
from django.utils import timezone  # 체크인 체크아웃 현재시간 확인 시켜주는거
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):

    """Reservation model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    # 체크인 체크아웃을 보고 현재 진행형인지 아닌지 확인 해야함
    def in_progress(self):
        now = timezone.now().date()
        return (
            now > self.check_in and now < self.check_out
        )  # true or false로 나타내라 check_in이 현재 시각보다

    # 높으면 True out 높으면 False
    in_progress.boolean = True  # X or 체크 표시 가능하게.
