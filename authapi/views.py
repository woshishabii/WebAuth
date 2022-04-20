from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import json

from . import models


def index(request):
    return render(request, 'authapi/index.html')


def instance_query(request, query_uuid, query_species):
    """
    This function is used to query the database for a specific instance of a query.
    :param request: The request object
    :param query_uuid: The UUID of the query
    :param query_species: species of the query
    :return: HttpResponse

    query_species is a string, separated by '|'.
    Available species:
    - name: Instance's description
    - version: Instance's version
    - force: If the instance is forced to update
    - views: Instance's views(If views included, it won't change)
    - link: New version's download link
    - announcement: Instance's announcement
    - update: New version's update log
    - md5: New version's file's md5
    """

    query = get_object_or_404(models.Instance, id=query_uuid)
    # response = json.dumps({"query_uuid": query_uuid, "query_species": query_species})
    species = query_species.split('|')
    response = {
        'uuid': str(query.id),
        'species': species,
        'result': {},
    }
    if 'name' in species:
        response['result']['name'] = query.name
    if 'version' in species:
        response['result']['version'] = query.version
    if 'force' in species:
        response['result']['force'] = query.force
    if 'views' in species:
        response['result']['views'] = query.views
    if 'link' in species:
        response['result']['link'] = query.link
    if 'announcement' in species:
        response['result']['announcement'] = query.announcement
    if 'update' in species:
        response['result']['update'] = query.update
    if 'md5' in species:
        response['result']['md5'] = query.md5

    return HttpResponse(json.dumps(response), content_type="application/json")


def test_base(request):
    return render(request, 'authapi/base.html')
