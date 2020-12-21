from django.urls import re_path
from .views import PlansView, PolicyDetailsView, MDPlanView,  MDDetailsView

urlpatterns = [
    re_path(r'^details/$', PolicyDetailsView.as_view()),
    re_path(r'^plan/\d+/$', PlansView.as_view()),
    re_path(r'^plan/mdplan/\d+/$', MDPlanView.as_view()),
    re_path(r'^mddetails/$', MDDetailsView.as_view()),

]