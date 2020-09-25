from django.conf import settings
from django.urls import URLPattern, URLResolver
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])


def ListEndpoints(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from ListEndpoints(l.url_patterns, acc + [str(l.pattern)])
    yield from ListEndpoints(lis[1:], acc)


@api_view(['GET'])
def get_endpoints(request: Request,) -> Response:
    list = []
    for p in ListEndpoints(urlconf.urlpatterns):
        list.append(''.join(p))
    return Response({"endpoints": list}, status=status.HTTP_400_BAD_REQUEST)
