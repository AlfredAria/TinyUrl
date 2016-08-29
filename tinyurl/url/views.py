from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from url.forms import LongUrlForm
from url.codec import Codec

import re

protocol = re.compile("(^http|^https|^ftp)")

def index(request):
    if request.method == 'POST':
        form = LongUrlForm(request.POST)
        if form.is_valid():
            long_url = append_protocol_name(form.cleaned_data['url'])
            shortUrl = Codec.long_to_short(long_url)
            return render(request, 'index.html', {'form': form, 'shortUrl': shortUrl})
    else:
        form = LongUrlForm()
    return render(request, 'index.html', {'form': form})

def lookup(request, base62):
    long_url = Codec.short_to_long(base62)
    return redirect(long_url, permenant=True)

def append_protocol_name(url):
    return "http://" + url if not protocol.search(url) else url
