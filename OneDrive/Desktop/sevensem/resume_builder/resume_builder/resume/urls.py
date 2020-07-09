from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('createresume', views.resumeForm, name='resumeform'),
    path('templates/<id>',views.templates,name='templates'),
    path('pdf/<id>', views.generate_view, name='pdf'),
    ]