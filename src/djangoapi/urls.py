from django.conf.urls import url, include
from django.contrib import admin

from updates.views import (
    json_example_view, 
    json_example_html_view, 
    JsonCBV, 
    JsonCBVmix, 
    SerializedDetailView, 
    SerializedListView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', json_example_view, name='json'),
    url(r'^json/', json_example_html_view, name='html'),
    url(r'^cbv/', JsonCBV.as_view(), name='cbv'),
    url(r'^mix/', JsonCBVmix.as_view(), name='mix'),
    url(r'^detail/', SerializedDetailView.as_view(), name='detail'),
    url(r'^list/', SerializedListView.as_view(), name='list'),
    url(r'^api/updates/', include('updates.api.urls')),
]
