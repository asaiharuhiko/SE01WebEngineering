from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("login",views.login_account,name="login"),
    path("logout",views.logout_account,name="logout"),
    path("create",views.create_account,name="create"),
    path("information",views.info_account,name="information")
]