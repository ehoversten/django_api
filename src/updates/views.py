import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.views.generic import View

from djangoapi.mixins import JsonResponseMixin

from .models import Update

# Create your views here.
''' STANDARD FUNCTION VIEW '''
# def   detail_view(request):
    # RETURN JSON DATA
    # return render(request, "", {})
    # return HttpResponse(get_template().render({''' context data '''}))

''' 
    Function Based View returning data/context as JSON data 
'''
def json_example_view(request):
    ''' URI - for REST API '''
    data = {
        "count" : 100,
        "content" : "Some new content",
    }
    return JsonResponse(data)

''' 
    Function Based View returning data/context in JSON form as HttpResponse 
'''
def json_example_html_view(request):
    ''' URI - for REST API '''
    data = {
        "count" : 100,
        "content" : "Some Other content",
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


''' 
    Class Based View returning data/context as JSON data 
'''
class JsonCBV(View):
    def get(self, request, *args, **kwargs): 
        data = {
            "count" : 100,
            "content" : "Some Class Based View content",
        }
        return JsonResponse(data)
        # --- OR as HttpResponse to view --- #
        # json_data = json.dumps(data)
        # return HttpResponse(json_data, content_type='application/json')

''' 
    Class Based View returning data/context as JSON data through a MIXIN 
'''
class JsonCBVmix(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs): 
        data = {
            "count" : 100,
            "content" : "Some Class Based Mixin View content",
        }
        return self.render_to_json_response(data)

''' 
    Serialized Class Based View returning data/context as JSON data 
'''
class SerializedDetailView(View):
    def get(self, request, *args, **kwargs): 
        # obj = Update.objects.get(id=1)
        # data = {
        #     "user" : obj.user.username, 
        #     "content" : obj.content,
        # }
        # json_data = json.dumps(data)
        # return HttpResponse(json_data, content_type='application/json')

        # --- OR --- # 
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj,], fields=('user', 'content'))
        print(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')

''' 
    Serialized Class Based View returning data/context as JSON data 
'''
class SerializedListView(View):
    def get(self, request, *args, **kwargs): 
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)
        json_data = data
        return HttpResponse(json_data, content_type='application/json')