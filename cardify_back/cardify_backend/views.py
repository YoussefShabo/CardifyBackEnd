from django.shortcuts import render

# Create your views here.

# def cardify_view(request):
#     return render(request, 'cardify_backend.html', {})
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics
from .serializers import DeckSerializer
from .models import Deck

from social_django.utils import psa

from requests.exceptions import HTTPError

class DeckList(generics.ListCreateAPIView):
    queryset = Deck.objects.all().order_by('id')
    serializer_class = DeckSerializer

class DeckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all().order_by('id')
    serializer_class = DeckSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
@psa()
def register_by_access_token(request, backend):
    token = request.data.get('access_token')
    user = request.backend.do_auth(token)
    print(request)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key
            },
            status=status.HTTP_200_OK,
            )
    else:
        return Response(
            {
                'errors': {
                    'token': 'Invalid token'
                    }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(['GET', 'POST'])
def authentication_test(request):
    print(request.user)
    return Response(
        {
            'message': "User successfully authenticated"
        },
        status=status.HTTP_200_OK,
    )