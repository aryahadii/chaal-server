from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from .views import SubchaalsViewSet, ThreadsList, ThreadRetrieve

router = routers.DefaultRouter()
router.register(r'subchaals', SubchaalsViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include(router.urls)),
    url(r'^threads/$', ThreadsList.as_view()),
    url(r'^thread/(?P<pk>[0-9]+)/$', ThreadRetrieve.as_view()),
]
