from django.http import HttpResponse
from django.shortcuts import render
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = this_dir
    my_context = {'page_path': my_title}
    html_ = 'home.html'
    return render(request, html_, my_context)