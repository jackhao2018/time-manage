from django.urls import re_path
from .views import PlansView, PolicyDetailsView

urlpatterns = [
    re_path(r'^plan/([a-zA-Z0-9-]+)/$', PlansView.as_view()),
    re_path(r'^details/([a-zA-Z0-9-]+)([a-zA-Z0-9-]+)|/$', PolicyDetailsView.as_view()),


]