"""groupchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views


from rest_framework import routers
from chat.views import UserViewSet,GroupViewSet,GroupCreate,GroupDetail,GroupMember,GroupChat,MessageLike

app_name = 'chat'

router = routers.DefaultRouter()
router.register(r'userlist', UserViewSet,basename='userlist')
router.register(r'grouplist',GroupViewSet,basename='grouplist')
router.register(r'groupcreate',GroupCreate,basename='groupcreate')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('group/<int:pk>/', GroupDetail.as_view(), name="GroupDetail"),
    path('group/<int:pk>/member/', GroupMember.as_view(), name="GroupMember"),
    path('group/<int:pk>/messages/', GroupChat.as_view(), name="GroupChat"),
    path('group/<int:group_id>/messages/<int:msg_id>/', MessageLike.as_view(), name="MessageLike"),
]
