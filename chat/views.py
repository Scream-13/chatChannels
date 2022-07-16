from django.shortcuts import redirect, render
from .models import Message, Room
from django.contrib.auth.decorators import login_required
from .forms import RoomForm
from django.template.defaultfilters import slugify


@login_required
def index(request):
    if request.method == 'POST':
        roomform = RoomForm(request.POST)
        if roomform.is_valid():
            name = roomform.cleaned_data['name']
            slug = slugify(name)
            Room.objects.create(name=name, slug=slug)
            return redirect('index')
    rooms = Room.objects.all()
    roomform = RoomForm()
    return render(request, 'index.html', {'rooms':rooms, 'roomform':roomform})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'chatroom.html', {
        'room': room,
        'messages':messages
    })

def base(request):
    return redirect('index')