from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
]
