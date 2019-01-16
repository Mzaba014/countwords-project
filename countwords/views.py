from django.http import HttpResponse
from django.shortcuts import render
import collections
import re


def home(request):
    return render(request, 'home.html')


def count(request):
    usertext = request.GET['usertext']
    # Removing special characters from the provided text
    re.sub('[^A-Za-z0-9 \\n]+', '', usertext)
    split_text = usertext.split()
    word_count = len(split_text)
    most_common = collections.Counter(split_text).most_common(3)
    return render(request, 'count.html', {'usertext': usertext, 'word_count': word_count, 'most_common': most_common})


def about(request):
    return render(request, 'about.html')
