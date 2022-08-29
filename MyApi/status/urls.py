

from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.StatusCreateListApiView.as_view()),
    path('status/<id>/', views.StatusDetailUpdateDestroyApiView.as_view()),

]
