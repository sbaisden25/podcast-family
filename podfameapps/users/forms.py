from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from podfameapps.podfame_main.models import  GuestProfile
from django.contrib.auth import get_user_model

non_allowed_usernames = ['abc']
# check for unique email & username

User = get_user_model()


class EditProfileForm(UserChangeForm):

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #occupation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    summary = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class': 'form-control'}))
    #profile_pic = forms.ImageField(required = False)
    about = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    interests = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pod_exp = forms.CharField(required = False, max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    why_user_pods = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))

    facebook_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    youtube_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = GuestProfile
        fields = ('name', 'location', 'summary', 'about', 'interests', 'pod_exp', 'why_user_pods', 'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')


""" 
choices = GuestAvailibility.objects.all().values_list('availibilityName', 'availibilityName')

availibility_list = []

for item in choices:
    availibility_list.append(item)
 """

class AddProfileForm(forms.ModelForm):

    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #occupation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    summary = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class': 'form-control'}))
    #profile_pic = forms.ImageField(required = False)
    about = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    interests = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pod_exp = forms.CharField(required = False, max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    why_user_pods = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))

    facebook_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    youtube_url = forms.CharField(required = False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = GuestProfile
        fields = ('name', 'location', 'summary', 'about', 'interests', 'pod_exp', 'why_user_pods', 'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')

    



class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("This is an invalid username, please pick another.")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    # def clean(self):
    #     data = super().clean()
    #     username = data.get("username")
    #     password = data.get("password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username
