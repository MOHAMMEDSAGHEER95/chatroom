from django.shortcuts import render

# Create your views here.

# chat/views.py
from django.shortcuts import render
from django.core.cache import cache


def index(request):
    return render(request, "chat/chat.html")


def room(request, room_name):
    if not request.session.session_key:
        request.session.save()
        request.session['username'] = request.session.session_key
        print(request.session.session_key)
    all_messages = cache.get(f'{room_name}-chat-messages', {})
    return render(request, "chat/chat.html", {"room_name": room_name, "all_messages": all_messages})