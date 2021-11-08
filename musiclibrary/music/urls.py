from . import views
from django.urls import path

urlpatterns = [
    path('music/', views.SongList.as_view()),
]