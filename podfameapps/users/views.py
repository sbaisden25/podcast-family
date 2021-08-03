from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import EditProfileForm, AddProfileForm, LoginForm, RegisterForm
from django.views import generic
from podfameapps.podfame_main.models import  GuestProfile
from django.views.generic import CreateView, DetailView
from django.contrib.auth import authenticate, login, logout, get_user_model

# Create your views here.

User = get_user_model()


class EditSettingsView(generic.UpdateView):
    model = User
    template_name = 'profilemanip/edit_settings.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user 




class EditProfilePageView(generic.UpdateView):
    model = GuestProfile
    template_name = 'profilemanip/edit_profile_page.html'
    fields = ['name', 'location', 'summary', 'about', 'interests', 'pod_exp', 'why_user_pods', 'facebook_url', 'instagram_url', 'twitter_url', 'youtube_url']
    success_url = reverse_lazy('home')




def AddProfileView(request,*args,**kwargs):
    form = AddProfileForm(request.POST or None)
    if form.is_valid():

        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        form = AddProfileForm()
    return render(request, "profilemanip/addprofile.html", {"form": form}) 
    success_url = reverse_lazy('home') 








def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1 # 1 == True
    return render(request, "forms.html", {"form": form})

def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/login")    