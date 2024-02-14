from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

class Fibonacci(viewsets.ViewSet):
    pagination_class = LimitOffsetPagination
    def get(self, request, fibonacci_number):
        try :
            fibonacci_number = int(fibonacci_number)
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
        # pagination part
            
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(fib_sequence,request)
        # result = paginator.get_paginated_response(paginated_queryset)
        return Response(paginated_queryset,status=status.HTTP_200_OK)


# from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class FibonacciAPIView(APIView):
#     pagination_class = LimitOffsetPagination
    
#     def get(self, request):
#         number = int(request.GET.get('number', 30))  # Default Fibonacci number is 30
#         limit = int(request.GET.get('limit', 20))     # Default limit is 20
#         offset = int(request.GET.get('offset', 0)) 
#         # Function to calculate Fibonacci numbers
#         def fibonacci(n):
#             a, b = 0, 1
#             fib_list = []
#             for _ in range(n):
#                 fib_list.append(a)
#                 a, b = b, a + b
#             return fib_list
        
#         # Calculate Fibonacci numbers   
#         fib_numbers = fibonacci(number)

#         start_index = offset
#         end_index = min(offset + limit, len(fib_numbers))
#         paginated_fib_numbers = fib_numbers[start_index:end_index]
#         return Response(paginated_fib_numbers)
#         # Paginate the Fibonacci numbers
#         # paginator = self.pagination_class()
#         # paginated_fib_numbers = paginator.paginate_queryset(fib_numbers, request)
        
#         # # Return paginated response
#         # return Response(paginator.get_paginated_response(paginated_fib_numbers))
