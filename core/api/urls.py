from django.urls import path
from expense import views


urlpatterns = [
    path('get-transactions/', views.get_transactions)
]