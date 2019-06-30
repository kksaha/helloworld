from django.urls import path
from . views import UserView

app_name = "user"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    #path('user/', UserView.as_view()),
    #path('<int:pk>', UserView.as_view()),
    #path('',UserView.as_view(), kwargs={'pk': None}),
    #path('^user/(?P<username>\w+)$', UserView.as_view()),
    path('hello/<str:user_name>/', UserView.as_view()),
    path('hello/<str:user_name>/', UserView.as_view()),
]

