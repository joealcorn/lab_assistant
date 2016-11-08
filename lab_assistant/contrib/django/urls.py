from django.conf.urls import include, url

from .views import mismatch_list, specific_mismatch

urlpatterns = [
    url(r'^$', mismatch_list),
    url(r'^result/(?P<result_id>[0-9]{19})/?$', specific_mismatch, name='specific_mismatch'),
]
