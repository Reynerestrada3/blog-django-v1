from .models import Publication
from django.views.generic import ListView, DetailView

# Create your views here.
class PublicationListView (ListView):
    model = Publication
    template_name = 'publications-list.html'

class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication-details.html'