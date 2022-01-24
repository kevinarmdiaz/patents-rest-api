from django.urls import path

from patents_api import views

urlpatterns = [
    path('patents/', views.PatentsGeneratorView.as_view()),
]
