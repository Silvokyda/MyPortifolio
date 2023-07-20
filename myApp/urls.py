from django.urls import path
from myPortfolio import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
      path('', views.main),
      path('resume/', views.resume),
      path('projects/', views.projects),
      path('contact/', views.contact)
]

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)