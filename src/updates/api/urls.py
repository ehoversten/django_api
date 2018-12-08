from django.conf.urls import url

from .views import (
    UpdateModelDetailAPI,
    UpdateModelListAPI,
)

urlpatterns = [
    # url(r'^$', json_example_view, name='json'),  # api/updates
    url(r'^$', UpdateModelListAPI.as_view()),
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPI.as_view()),
]
