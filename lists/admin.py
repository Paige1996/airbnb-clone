from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    pass
    """List Admin Definition"""


# Register your models here.
