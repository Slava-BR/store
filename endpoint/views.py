import json

from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import get_object_or_404

from endpoint.models import Cloth


def get_json(object, server, full=False):
    d = {
        'title': object.title,
        'collection': f'{server}/collection/{object.slug_title}',
        'type': f'{server}/type/{object.slug_title}',
        'price': object.price,
        'image': f'{server}/image/{object.slug_title}',
    }
    if full:
        d['size'] = f'{server}/size/{object.slug_title}'
        d['textile'] = f'{server}/textile/{object.slug_title}'
        d['material'] = f'{server}/material/{object.slug_title}'
    return d


def detail(requests, slug_title):
    return JsonResponse(get_json(get_object_or_404(Cloth, slug_title=slug_title), requests.headers['HOST'], full=True))


# Create your views here.
def main(requests):
    data = Cloth.objects.filter(main=True)
    result = {}
    for i in data:
        result[i.title] = get_json(i, requests.headers['HOST'])
    return JsonResponse(result)


def collection(requests):
    data = Cloth.objects.filter(collections=requests.GET.get('collections'))
    result = {}
    for i in data:
        result[i.title] = get_json(i, requests.headers['HOST'])
    return JsonResponse(result)


def image(requests, slug_title):
    return FileResponse(open(get_object_or_404(Cloth, slug_title=slug_title).image.path, 'rb'))


def price(requests, slug_title):
    return HttpResponse(get_object_or_404(Cloth, slug_title=slug_title).price)


def title(requests, slug_title):
    return HttpResponse(get_object_or_404(Cloth, slug_title=slug_title).title)


def type(requests, slug_title):
    return HttpResponse(get_object_or_404(Cloth, slug_title=slug_title).type)


def size(requests, slug_title):
    return HttpResponse(get_object_or_404(Cloth, slug_title=slug_title).size["size"])


def textile(requests, slug_title):
    return HttpResponse(get_object_or_404(Cloth, slug_title=slug_title).textile)


def material(requests, slug_title):
    return HttpResponse(get_object_or_404(Cloth, slug_title=slug_title).material)
