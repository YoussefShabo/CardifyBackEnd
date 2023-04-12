from django.contrib import admin
from django.urls import path, include, re_path
from . import views

# urlpatterns = [
#     path('cardify', views.cardify_view.as_view(), name="cardify_view"),
# ]
app_name = 'cardify_backend'

urlpatterns = [
    re_path('api/register-by-access-token/' + r'social/(?P<backend>[^/]+)/$', views.register_by_access_token),
    path('api/authentication-test/', views.authentication_test),
    path('api/decks', views.DeckList.as_view(), name='deck_list'),
    path('api/decks/<int:pk>', views.DeckDetail.as_view(), name='deck_detail'),
]