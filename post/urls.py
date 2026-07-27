from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("",views.index,name="index"),
    path("create/",views.create,name="create"),
    path("post/<int:id>/",views.detail,name="detail")
]