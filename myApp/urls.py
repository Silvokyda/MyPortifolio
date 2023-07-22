from django.urls import path
from myPortfolio import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),  
    path('contact/submit/', views.contact_form_submission, name='contact_form_submission'), 
]


urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)