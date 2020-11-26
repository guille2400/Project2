from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, loader
from files.functions import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
	template = loader.get_template("index.html")
	return HttpResponse(template.render())

@csrf_exempt
@require_http_methods(["POST"])
def search(request):
	search_terms = request.POST.get('searchTerms')
	tweets = similar_n(search_terms, 10)
	return JsonResponse({'tweets': [x[1] for x in tweets]})
