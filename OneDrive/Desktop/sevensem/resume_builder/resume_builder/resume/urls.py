from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('createresume', views.resumeForm, name='resumeform'),
    path('apilist', views.apilist, name='apilist'),
    path('templates/<id>',views.templates,name='templates'),

    path('pdf_view/<id>', views.ViewPDF.as_view(), name="pdf_view"),
    ]