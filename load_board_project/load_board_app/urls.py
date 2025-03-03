from django.urls import path
from load_board_app import views

urlpatterns = [
    path('', views.load_board_view, name='load_board')
]