from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
# * Admin : admin.py에서 model을 가져오려면 @admin register(models.User)..
# 즉 decoratro을 class 와 함께 해줘야함.  models.User를  Class CustomUserAdmin(UserAdmin)라는 클래스에 적용하겠다는 뜻.  @admin register(models.User)이거 대신 admin.site.register(models.User, CustomUserAdmin) 써도됨. 이것도 동일한 말.
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
@admin.register(models.User)  # decorator. admin패널에서 이 user을 보고싶어
class CustomUserAdmin(UserAdmin):  # customUserAdmin으로 user을 컨트롤 UserAdmin은 상속받음

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (  # userAdmin은 이미 장고가 자동으로 가지고 있다. 그거에다가 filedset이라는 내가만든 세트도 같이 화면에 적용해달라는것임
        # 윗 부분이 userAdmin, 밑에있는 filedset이 내가 만든 세트
        (
            "Custom profile",  # 필드의 제목
            {
                "fields": (  # 필드 내용
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)  # 옆꿀떼기에 보이는거

    # 처음 raw에 어떻게 보여질지
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
