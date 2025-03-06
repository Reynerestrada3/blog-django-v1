from django.urls import path
from .views import PublicationListView

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
]