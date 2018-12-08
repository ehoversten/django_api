import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# STANDARD FUNCTION VIEW
# def   detail_view(request):
    # RETURN JSON DATA
    # return render(request, "", {})
    # return HttpResponse(get_template().render({''' context data '''}))

def json_example_view(request):
    ''' URI - for REST API '''
    data = {
        "count" : 100,
        "content" : "Some new content",
    }
    return JsonResponse(data)

def json_example_html_view(request):
    ''' URI - for REST API '''
    data = {
        "count" : 100,
        "content" : "Some Other content",
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')