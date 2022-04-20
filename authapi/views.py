from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return render(request, 'authapi/index.html')


def about(request):
    return render(request, 'authapi/about.html')


def instance_query(request, query_uuid, query_species):
    response = json.dumps({"query_uuid": query_uuid, "query_species": query_species})
    return HttpResponse(response)


def test_base(request):
    return render(request, 'authapi/base.html')
