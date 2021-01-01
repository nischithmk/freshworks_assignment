from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_items,success,failure,get_single_key,delete_key

urlpatterns = {
    path('', manage_items, name="items"),
    path('success',success,name = "success"),
    path('failure',failure,name = "failure"),
    path('send_get_request',get_single_key,name = "key"),
    path('send_delete_request',delete_key,name = "delete_key"),
}
urlpatterns = format_suffix_patterns(urlpatterns)