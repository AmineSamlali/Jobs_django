

from django.urls import path
from  .  import views

urlpatterns = [
    path('profile/', views.profile_shower , name='profile_user'),
    path('profile/edit', views.profile_edit , name='profile_edit'),
    path('signup', views.signup , name='signup'),
    path('dash',views.dash, name='dash'),
    path('dash/edit/<str:slug>',views.dash_edit, name='dash_edit'),

]