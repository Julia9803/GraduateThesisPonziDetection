from django.http.response import JsonResponse
from model_RF import RandomForest


def index(request):
    request.encoding = 'utf-8'
    if 'method' in request.GET and request.GET['method']:
        method = request.GET['method']
    else:
        method = "ALL"
    if 'N' in request.GET and request.GET['N']:
        N = request.GET['N']
    else:
        N = 1
    result = RandomForest(method, N)
    return JsonResponse(result)
