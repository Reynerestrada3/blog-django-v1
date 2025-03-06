from .models import Publication
from django.views.generic import ListView

# Create your views here.
class PublicationListView (ListView):
    model = Publication
    template_name = 'publications-list.html'
