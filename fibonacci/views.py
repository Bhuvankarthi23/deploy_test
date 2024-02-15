from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class Fibonacci(viewsets.ViewSet):
    pagination_class = CustomPagination

    def get(self, request, fibonacci_number):
        try :
            fibonacci_number = int(fibonacci_number)
            if fibonacci_number < 0 :
                return Response({"message":"Number should be positive"},status = status.HTTP_400_BAD_REQUEST)
            if fibonacci_number > 1:
                fib_sequence = [0, 1]
            elif fibonacci_number == 1:
                fib_sequence = [0]
            else:
                fib_sequence = []
                
            while len(fib_sequence) < fibonacci_number:
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) 
        except :
            return Response({"message":"Entry should be a number"},status=status.HTTP_200_OK)
        
        paginator = self.pagination_class()
        paginated_sequence = paginator.paginate_queryset(fib_sequence, request)
        response = paginator.get_paginated_response(paginated_sequence)
        
        # if paginator.get_next_link():
        #     response.data['next_page'] = paginator.get_next_link()
        # pagination part
            
        # paginator = self.pagination_class()
        # paginated_queryset = paginator.paginate_queryset(fib_sequence,request)        
        
        return response


