from django.db import models
from core import models as core_models

# Create your models here.

#  대화에 침여자와 메시지 보기
class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField(
        "users.User", related_name="conversation", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            # 모든 paricipants, 모든 users의 querySet을 줌. 대화에서 participants가 있는데 그게
            # 딱 두명이겠지?
            usernames.append(user.username)
            # user에 있는 username을 가져와 usernames에 집어 넣는다.
        return ", ".join(usernames)  # 대화 참여자들의 "," 콤마로로 나열해서 join 하면 string문자를 읽을수 있음

    def count_messages(self):
        return self.messages.count()
        # message가 어디서 온거냐? 밑에 클래스 message는 conversation을 FK로 사용하고 있고 그 conversation의 FK안에 related_name이 "messages"
        # 이기 때문에 자유자제로 쓸 ㅅ ㅜ있음

    count_messages.short_description = "number of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "number of participants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
