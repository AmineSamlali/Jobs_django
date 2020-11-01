from django.urls import path
from . import views


urlpatterns = [
    path('post',views.post_ajob, name='POST_JOB'),
    path('',views.test_project , name='test' ),
    path('<str:slug>' , views.post_id , name='id'),

]