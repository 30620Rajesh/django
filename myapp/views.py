from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myapp_home(request):
    return HttpResponse("""
    <h1> Hello world </h1>
                        <h2> I am learning django</h2>
    """)