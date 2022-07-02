from django.shortcuts import render
from django.http import HttpResponse
# import datetime
# from .models import employee
# from .Serialiser import empserial
# from rest_framework import generics


# Create your views here.
#
def greet(request):
    msg = '<h1>This is the message from Django first app</h1>'
    return HttpResponse(msg)

# #
# def greet2(request):
#
#     return HttpResponse('<b><i>good morning</i></b>')
#
# def acthtml(request):
#     return render(request,'filehtml.html')
#
# def acthtml2(request):
#     return render(request,'formhtml.html')
# #
#
# def acthtml3(request):
#     return render(request,'googlehtml.html')

def acthtml4(request):
    return render(request,'loginpage.html')

def acthtml5(request):
    return render(request,'registorpage.html')

def acthtml6(request):
    return render(request,'pollpage.html')

def acthtml7(request):
    return render(request,'profilepage.html')


# def employee(request):
#     name = 'komal'
#     id = '12345'
#     salary = '40000'
#     experience = '2 years'
#     date = datetime.datetime.now()
#     mydict = { 'name': name,'id':id,'salary':salary,'experince':experience,'date': date}
#
#     return render(request,'employee.html',context=mydict)
#
#
# class display(generics.ListCreateAPIView):
#     serializer_class = empserial
#     queryset =employee.objects.all()
