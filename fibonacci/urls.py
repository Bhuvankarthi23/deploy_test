from django.urls import path

from .views import Fibonacci

urlpatterns = [
    path("number/<int:fibonacci_number>/",Fibonacci.as_view({"get": 'get'}) , name="index"),
]