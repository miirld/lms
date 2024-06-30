from django.contrib.auth import get_user_model
from django.contrib.auth import login

from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from knox.views import LoginView as KnoxLoginView


from .serializers import AuthUserSerializer, AuthSerializer, ExtendedUserSerializer









@api_view(['GET'])
def account (request):
    user = get_user_model().objects.get(id=request.user.id)
    serializer = ExtendedUserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def me (request):
    return Response ({
        'id': request.user.id,
        'role': request.user.role
    })



class CreateUserView(generics.CreateAPIView):
    serializer_class = AuthUserSerializer


class LoginView(KnoxLoginView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)    


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = AuthUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
