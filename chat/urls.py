from chat import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("add-username/", views.addusername, name="add-username"),
    path("<str:room_name>/", views.room, name="room"),
]