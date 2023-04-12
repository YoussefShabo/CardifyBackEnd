from django.contrib import admin
from django.urls import path, include
from . import views

# urlpatterns = [
#     path('cardify', views.cardify_view.as_view(), name="cardify_view"),
# ]
app_name = 'cardify_backend'

urlpatterns = [
    re_path('api/register-by-access-token/' + r'social/(?P<backend>[^/]+)/$', views.register_by_access_token),
    path('api/authentication-test/', views.authentication_test),
]