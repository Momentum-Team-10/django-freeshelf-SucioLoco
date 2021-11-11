from django.shortcuts import render, redirect
from .models import Book
from django.http import HttpResponse

def homepage (response):
    list_o_books = Book.objects.all().order_by("created_at")
    return list_o_books
# Create your views here.
