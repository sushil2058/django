from django.contrib import admin
from ssebs import views
from django.urls import path
from django.urls import reverse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.ssebs_index, name="ssebs_index"),
    path("<int:pk>/", views.ssebs_detail, name="ssebs_detail"),
    path("notice/", views.noticees, name="noticee"),
   
]