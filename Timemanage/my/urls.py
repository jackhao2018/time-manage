from django.urls import re_path
from .views import CollectView, MDcollectView


urlpatterns = [
    re_path(r'^collect/$', CollectView.as_view()),
    re_path(r'^mdcollect/$', MDcollectView.as_view()),
]