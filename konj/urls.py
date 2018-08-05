from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^explore/', include('explore.urls')),
    url(r'^post/', include('post.urls')),
]
