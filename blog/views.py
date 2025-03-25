from .models import Publication
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'publications-list.html'  

class PublicationDetailView(LoginRequiredMixin, DetailView):
    model = Publication
    template_name = 'publication-details.html'  

class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'publication-create.html'  
    fields = ['title', 'body', 'author']  

class PublicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Publication
    template_name = 'publication-update.html'  
    fields = ['title', 'body']

class PublicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Publication
    template_name = 'publication-delete.html'
    success_url = reverse_lazy('publications-list')