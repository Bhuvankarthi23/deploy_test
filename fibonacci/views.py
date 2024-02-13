from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework import viewsets
class Fibonacci(viewsets.ViewSet):
    def get(self, request, fibonacci_number):
        if fibonacci_number > 1:
            fib_sequence = [0, 1]
        elif fibonacci_number == 1:
            fib_sequence = [0]
        else:
            fib_sequence = []
            
        while len(fib_sequence) < fibonacci_number:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) 
        return Response({"fibonacci numbers are":fib_sequence},status=status.HTTP_200_OK)