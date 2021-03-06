"""adopteitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
import views
from authentication.views import AccountViewSet, LoginView, LogoutView

from django.contrib.auth import get_user_model
User = get_user_model()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Animal', views.AnimalViewSet, base_name="Animal")
router.register(r'Persona', views.PersonaViewSet)
router.register(r'FormularioAdopcion', views.FormularioAdopcionViewSet)
router.register(r'AdoptarAnimal', views.AdoptarAnimalViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'Subscripcion', views.SubscripcionViewSet)
router.register(r'Ipn', views.IpnViewSet)
urlpatterns = [
 url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
   url(r'^', include(router.urls)),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   url(r'^login/$', LoginView.as_view(), name='login'),
   url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
