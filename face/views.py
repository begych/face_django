# import os
import subprocess
# import time

import psutil
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth
from django.http.response import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from face_recognize.headshot import FaceAdd
from .camera import VideoCamera, VideoCamera_2, gen
from .models import *


def index(request):
    subprocess.call('/home/mtmerkez-7/PycharmProjects/face_django/face_recognize/start.sh', shell=True)
    return render(request, 'lock_screen.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Maglumatlaryňyzy ýalnyş girizdiňiz!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def HomePage(request):
    return render(request, 'data_table.html')


def livefe(request):
    subprocess.call('/home/mtmerkez-7/PycharmProjects/face_django/face_recognize/stop.sh', shell=True)
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')


def livefe_2(request):
    subprocess.call('/home/mtmerkez-7/PycharmProjects/face_django/face_recognize/stop.sh', shell=True)
    return StreamingHttpResponse(gen(VideoCamera_2()), content_type='multipart/x-mixed-replace; boundary=frame')


# class HomePage(LoginRequiredMixin, ListView,):
#     model = Person
#     template_name = 'data_table.html'
#     context_object_name = 'people'
#     # paginate_by = 4
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # get_in_out = Get_in_out.objects.all()
#         # context['out_in'] = get_in_out
#         return context


@login_required(login_url='login')
def register(request):
    if not is_running("/home/mtmerkez-7/PycharmProjects/face_django/face_recognize/Camera.py"):
        subprocess.call('/home/mtmerkez-7/PycharmProjects/face_django/face_recognize/start.sh', shell=True)
    subprocess.call("", shell=True)
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        profession = request.POST['profession']
        image = request.FILES.get('image_upload')
        person_user = Person.objects.create(name=name, surname=surname, profession=profession, image=image)
        person_user.save()
        FaceAdd(person_user.name + '_' + person_user.surname, person_user.id)
        return redirect('home_page')
    else:
        return render(request, 'add_profile.html')


class PersonView(LoginRequiredMixin, DetailView):
    model = Person
    template_name = 'person_view.html'
    context_object_name = 'people'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # get_in_out = Get_in_out.objects.all()
        # context['out_in'] = get_in_out
        return context


class DataChangeView(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['name', 'surname', 'profession', 'image']
    template_name = 'data_change.html'


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'delete.html'
    success_url = reverse_lazy('home_page')


def admin_logout(request):
    auth.logout(request)
    return redirect('/')


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(exception):
    data = {}
    return render('500.html', data)


def error_403(request, exception):
    data = {}
    return render(request, '403.html', data)


def error_400(request, exception):
    data = {}
    return render(request, '400.html', data)


def is_running(script):
    for q in psutil.process_iter():
        if q.name().startswith('python'):
            if len(q.cmdline()) > 1 and script in q.cmdline()[1] and q.pid != os.getpid():
                return True
    return False
