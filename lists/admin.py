from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    list_display = ("name", "user", "count_rooms")
    search_fields = ("^name",)

    filter_horizontal = ("rooms",)
    # 필드에서 여러 값을 입력하고 싶을 때 ManyToManyField를 사용하면 다중 선택 박스가 나타나 여러 개를 선택할 수는 있다.
    # 하지만 값이 수백개라면 다루기 힘들 것이다. 장고는 그것을 제공함
