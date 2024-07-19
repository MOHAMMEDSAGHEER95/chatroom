from django.shortcuts import render, redirect

# Create your views here.

# chat/views.py
from django.shortcuts import render
from django.core.cache import cache

from chat.models import User


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    if not request.session.session_key:
        request.session.save()
        request.session['username'] = request.session.session_key
        print(request.session.session_key)
    if request.session.session_key not in request.session:
        return render(request, "chat/newuser.html", {"room_name": room_name})
    all_messages = cache.get(f'{room_name}-chat-messages', {})
    users = User.objects.all()
    return render(request, "chat/chat.html", {"room_name": room_name, "all_messages": all_messages,
                                              'name':request.session[request.session.session_key], 'users': users})


def addusername(request):
    if not request.session.session_key:
        request.session.save()
    if request.method == 'POST':
        username = request.POST.get('username')
        User.objects.create(username=username)
        room_name = request.POST.get('room_name')
        request.session[request.session.session_key] = username
        return redirect(f'/chat/{room_name}/')
    else:
        return render(request, 'index.html')