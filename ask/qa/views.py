
from django.http import HttpResponse


def test(request, *args, **kwargs):
	return HttpResponse("Hello, world. You're at the polls index.")


def not_found(request):
	return HttpResponse(status=404)

