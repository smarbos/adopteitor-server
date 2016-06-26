from rest_framework import status, views, permissions, viewsets
from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer
from django.http import HttpResponse
import json
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            response = HttpResponse()
            response.write(serializer.validated_data)
            response.status_code=201
            return response

        response = HttpResponse()
        response.write(serializer)
        response.status_code=400
        return response


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                response = HttpResponse()
                response.write("This account has been disabled.")
                response.status_code=401
                return response
        else:
            response = HttpResponse()
            response.write("Username/password combination invalid.")
            response.status_code=401
            return response

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        response = HttpResponse()
        response.status_code=204
        return response
