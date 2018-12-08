from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# STANDARD FUNCTION VIEW
# def detail_view(request):
    # RETURN JSON DATA
    # return render(request, "", {})
    # return HttpResponse(get_template().render({''' context data '''}))

def update_model_detail_view(request):
    ''' URI - for REST API '''
    data = {
        "count" : 100,
        "content" : "Some new content",
    }
    return JsonResponse(data)