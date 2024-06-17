from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("js/", include("js.urls")),
    path("admin/", admin.site.urls),
]