from django.conf.urls import url
from account import views as account_views

urlpatterns = [
    url(r'^login/$', account_views.login_user, name="login_user"),
    url(r'^logout/$', account_views.logout_user, name="logout_user"),
]