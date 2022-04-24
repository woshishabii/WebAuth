from django.urls import path

from . import views

app_name = 'docs'
urlpatterns = [
    path('', views.index, name='index'),
    path('getting-started/quick-start/', views.quick_start, name='quick-start'),
    path('getting-started/build-tools/', views.build_tools, name='build-tools'),
]