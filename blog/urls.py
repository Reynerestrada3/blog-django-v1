from django.urls import path
from .views import PublicationListView, PublicationDetailView

urlpatterns = [
    path('', PublicationListView.as_view(), name='publications-list'),
    path('publication/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
]