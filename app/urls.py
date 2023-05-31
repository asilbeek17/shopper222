from django.urls import path
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', Categories.as_view(), name='categories'),
    path('contact/', contact, name='contact'),
    path('single/<int:pk>/', Single.as_view(), name='single'),
    path('confirm/', confirm, name='confirm'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
]
