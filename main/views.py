from django.shortcuts import render, redirect
from .models import Process
from .forms import ProcessForm


def index(request):
    processes = Process.objects.order_by('-id')[:]
    return render(request, 'main/index.html', {'title': 'Main page', 'processes': processes})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProcessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'incorrectly filled'

    form = ProcessForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
