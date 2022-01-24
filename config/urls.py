"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# setting에 있는 설정들을 가져오겠다
# static file들을 제공하는 걸 도움
urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.DEBUG:  # 만약 DEBUG가 트루 일때, 즉 내 개발자 용에만 쓸수있는 설정일경우. (서버에다가 개발자 모드로 설정하지 말기 )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # 사진 경로를 주기위해. urlpatters += 뜻은 위에있는 거에 하나를 더 추가한다는 뜻임.
