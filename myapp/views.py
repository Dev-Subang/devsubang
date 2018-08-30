from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from myapp.models import Lesson, Course

from myapp.forms import SignUpForm

def index(request):
    if not request.user.is_authenticated():
        return render(request,'index.html')
    else:
        return render(request,'index_login.html')

def signup(request):
            if request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=raw_password)
                    login(request, user)
                    return redirect('index')
            else:
                form = SignUpForm()
            return render(request, 'registration/signup.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

def pembelajaran(request):
    course = Course.objects.all().order_by('order')
    return render(request, 'pembelajaran.html', {'courses': course})

@login_required
def course(request, id, lesson_id):
    lessons = Lesson.objects.filter(course__id=id).order_by('order')
    course = Course.objects.filter(id=id)[0]
    active_lesson = int(lesson_id)
    if lesson_id == '0':
        content = course.summary
    else:
        data = Lesson.objects.filter(id=lesson_id).order_by('order')[0]
        content = data.konten
    return render(request, 'lesson.html', {'lessons': lessons,
                                           'course': course,
                                           'content': content,
                                           'active_lesson': active_lesson}
                  )


# Create your views here.
