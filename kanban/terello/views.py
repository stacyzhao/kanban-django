from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'terello/index.html'


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('status')
    serializer_class = TaskSerializer

def logmein(request):
   username = request.GET.get('username')
   password = request.GET.get('pwd')
   stayloggedin = request.GET.get('stayloggedin')
   if stayloggedin == "true":
       pass
   else:
       request.session.set_expiry(0)
   user = authenticate(username=username, password=password)
   if user is not None:
       if user.is_active:
           login(request, user)
           return HttpResponse('fine')
       else:
           return HttpResponse('inactive')
   else:
       return HttpResponse('bad')
# def ajax_registration(request):
#     obj = {
#         'login_form': AuthenticationForm(),
#         'registration_form': RegistrationForm(),
#     }
#     return render(request, 'common/ajax_registration.html', obj)

# class TaskList(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('status')
#     serializer_class = TaskSerializer
#
#
# class TaskDetail(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('priority')
#     serializer_class = TaskSerializer
