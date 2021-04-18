from django.shortcuts import render
from .forms import *
def index(request):
    return render(request, 'index.html')

def request_obj(request):
    data = {
        'path': request.path,
        'full_path': request.get_full_path(),
        'host': request.get_host(),
        'method': request.method,
        'is_secure': request.is_secure()
    }
    return render(request, 'request-obj.html', data)

def form_get(request):
    q = request.GET.get('q', None)
    return render(request, 'form-get.html', {'q': q})

def form_post(request):
    if 'firstname' not in request.POST:
        return render(request, 'form-post.html')
    else:
        data = {
            'fname': request.POST.get('firstname', None),
            'lname': request.POST.get('lastname', None)
        }
        return render(request, 'form-post.html', data)

def search(request):
    form = SearchForm(request.GET)
    data = {'form': form}
    return render(request, 'search.html', data)

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()
        
    return render(request, 'product.html', {'form': form})