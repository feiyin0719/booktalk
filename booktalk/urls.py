"""booktalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.views.static import serve

import xadmin
from django.conf.urls import url, include
from rest_framework import routers

from api.views import Test1ViewSet, Test2ViewSet, Test3ViewSet, BookReadViewSet, BookShareViewSet, UserViewSet
from booktalk import settings

xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()
router = routers.DefaultRouter()
router.register(r'test1s', Test1ViewSet,base_name='test1')
router.register(r'test2s', Test2ViewSet,base_name='test2')
router.register(r'test3s', Test3ViewSet,base_name='test3')
router.register(r'bookreads', BookReadViewSet,base_name='bookread')
router.register(r'bookshare', BookShareViewSet,base_name='bookshare')
router.register(r'users',UserViewSet,base_name='myuser')
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^media/(?P<path>.*)/$', serve, {"document_root": settings.MEDIA_ROOT}),
]
