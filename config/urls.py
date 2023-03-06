"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('acc/', include("acc.urls")),
    path('board/', include("board.urls")),
    path('trans/', include('trans.urls')),
    path('vote/', include("vote.urls")),
    path('book/', include("book.urls")),
    path('tts/', include("tts.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 대형 서비스의 경우 많이 사용하는 urls를 위로 빼두면 속도가 빨라진다