# from django.middleware.gzip import GZipMiddleware
# import gzip
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators import gzip

from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

from face_recognize.headshot import FaceAdd
from django.http.response import StreamingHttpResponse


from .camera import VideoCamera, gen
from .camera_2 import VideoCamera_2, gen_2


def index(request):
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
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')


def livefe_2(request):
    return StreamingHttpResponse(gen_2(VideoCamera_2()), content_type='multipart/x-mixed-replace; boundary=frame')

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
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        profession = request.POST['profession']
        image = request.FILES.get('image_upload')
        person_user = Person.objects.create(name=name, surname=surname, profession=profession, image=image)
        person_user.save()
        FaceAdd(person_user.name+'_'+person_user.surname, person_user.id)
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



