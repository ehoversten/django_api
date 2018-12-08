from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel

'''
    CREATING - UPDATING - DELETING - RETRIEVING (1) -- UPDATE MODEL
'''
class UpdateModelDetailAPI(View):
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")

    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")


'''
    RETRIEVING (All) -- UPDATE MODEL
'''
class UpdateModelListAPI(View):
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type="application/json")