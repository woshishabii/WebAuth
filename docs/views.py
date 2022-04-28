from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'docs/index.html')


def quick_start(request):
    return render(request, 'docs/getting-started/quick-start.html')


def build_tools(request):
    return render(request, 'docs/getting-started/build-tools.html')
