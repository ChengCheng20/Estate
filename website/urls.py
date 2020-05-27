from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('agentsingle.html', views.agentsingle, name='agentsingle'),
    path('agentgrid.html', views.agentgrid, name='agentgrid'),
    path('blogsingle.html', views.blogsingle, name='blogsingle'),
    path('bloggrid.html', views.bloggrid, name='bloggrid'),
    path('propertysingle.html', views.propertysingle, name='propertysingle'),
    path('propertygrid.html', views.propertygrid, name='propertygrid'),
]