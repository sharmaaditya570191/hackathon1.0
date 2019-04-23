from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.post_list, name='post_list'),
    path('signup/', views.SignUp.as_view(), name='signup'),

]
