from .views import BranchesViewSet, PostsList, PostRetrieve

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'branches', BranchesViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include(router.urls)),
    url(r'^posts/$', PostsList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', PostRetrieve.as_view()),
]
