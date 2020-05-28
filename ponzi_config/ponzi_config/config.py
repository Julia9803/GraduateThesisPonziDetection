from django.http.response import JsonResponse
from model_RF import RandomForest
import os
import json

basepath = "res/res3/"
root_dir = os.path.dirname(os.path.abspath('.'))
curr_dir = "/ponzi_config/ponzi_config/"


def config(request):
    request.encoding = 'utf-8'
    if 'method' in request.GET and request.GET['method']:
        method = request.GET['method']
    else:
        method = "ALL"
    if 'N' in request.GET and request.GET['N']:
        N = request.GET['N']
    else:
        N = 1
    if 'model' in request.GET and request.GET['model']:
        model = request.GET['model']
    else:
        model = "LightGBM"
    file = root_dir + curr_dir + basepath + method + str(N) + model + ".json"
    print("read ", file)
    if not os.path.exists(file):
        RandomForest(method, N)
    with open(file, 'r') as f:
        result = json.load(f)
        newres = {}
        for each in result:
            for item in result[each]:
                newres[each] = round(result[each]["0"], 4)
    return JsonResponse(newres)
