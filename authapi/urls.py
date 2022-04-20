from django.urls import path

from . import views

app_name = 'authapi'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('api/getInstance/<str:query_uuid>/<str:query_species>', views.instance_query, name='instance_query'),

    # Testing
    # path('test/base', views.test_base, name='test_base'),
]
