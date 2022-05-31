from django.urls import path
from BlogApp.views import index_view, citation_view, contact_view

urlpatterns = {
    path('', index_view, name='home'),
    path('citation/', citation_view, name='citation'),
    path('contact/', contact_view, name='contact'),
}