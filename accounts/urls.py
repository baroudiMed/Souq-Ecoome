from django.urls import path
from . import views
from django.conf.urls import url
app_name='accounts'
urlpatterns = [
    url(r'^register/$', views.user_register, name='register' ),
    path('<slug:slug>',views.profile,name='profile'),
]