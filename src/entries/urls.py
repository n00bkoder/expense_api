from . import views
from django.urls import path


urlpatterns = [

    path('', views.EntryView.as_view()),
    path('<int:pk>/', views.EntryDetail.as_view()), 

]