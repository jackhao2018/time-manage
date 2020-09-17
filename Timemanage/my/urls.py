from django.urls import re_path
from .views import CollectView

urlpatterns = [
    re_path(r'^collect/$', CollectView.as_view()),
    # re_path(r'^db/$', DatabaseChange.as_view()),
    # re_path(r'^shares/$', Shares.as_view()),
    # re_path(r'^capital/$', Capital.as_view()),
    # re_path(r'^channel/$', Channels.as_view()),
    # re_path(r'^protocol/$', Protocol.as_view()),
    # re_path(r'^secuacc/$', Secuacc.as_view()),
    # re_path(r'^resetpwd/$', ResetPwd.as_view()),  #
    # re_path(r'^setrisktime/$', SetRiskTime.as_view()),
]