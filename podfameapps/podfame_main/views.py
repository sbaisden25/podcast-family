from django.shortcuts import render, get_object_or_404
from .models import GuestProfile
from django.views.generic import ListView, DetailView

# Create your views here.

class GuestDirectoryView(ListView):

    model = GuestProfile
    paginate_by = 4
    template_name = "directory/guestdir.html"


class GuestProfileView(DetailView):

    model = GuestProfile
    template_name = "profile/guestprof.html"

    def get_context_data(self, *args, **kwargs):
        #users = GuestProfile.objects.all()
        context = super(GuestProfileView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(GuestProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


