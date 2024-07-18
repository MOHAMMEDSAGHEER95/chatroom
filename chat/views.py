from django.shortcuts import render

# Create your views here.

# chat/views.py
from django.shortcuts import render
from django.core.cache import cache


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    all_messages = cache.get(f'{room_name}-chat-messages', {})
    return render(request, "chat/room.html", {"room_name": room_name, "all_messages": all_messages})