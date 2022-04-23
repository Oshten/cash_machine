from django.urls import path

from cash_register import views

urlpatterns = [
    path('cash_machine/', views.MakeChek.as_view()),
    path('media/<str:name>', views.get_chek),
]