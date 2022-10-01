from django.shortcuts import render, redirect
from .forms import signinform
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import friend, message
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'main/index.html')
def login(request):
    return render(request,'main/login.html')
#-------------------------------------------------------------------------------------------------
class signinview(generic.FormView):
    template_name = 'main/signin.html'
    form_class = signinform 
    success_url = '/friends'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class loginview(generic.FormView):
    template_name = 'main/login.html'
    form_class = AuthenticationForm
    success_url = '/friends'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super().form_valid(form)


#-------------------------------------------------------------------------------------------------
def friends(request):

    return render(request,'main/friends.html')


class friendsview(LoginRequiredMixin,generic.ListView):
    model = message
    template_name = "main/friends.html"
    
    def get_queryset(self):
        friends = friend.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user)).order_by('-created')
        return friends


    def get_context_data(self,*args,**kwargs):
        context = super(friendsview,self).get_context_data(*args,**kwargs)
        query = friend.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user)).order_by('-created')
        for object in query:
            try:
                if object.user1 == self.request.user:
                    name = object.user2.username
                else:
                    name = object.user1.username
                latest_message = message.objects.filter(friend=object).latest('created')
                context[name] = latest_message.content
            except:
                continue
        return context