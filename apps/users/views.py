from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer
from itt_core.wsgi import sio

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    """
    get:
    Return a list of all the existing users.
    Requires Bearer token authentication.

    post:
    Create a new user instance.
    """
    queryset = UserModel.objects.order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Returns a list of permission depending on the HTTP method.
        """
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [AllowAny()]


class UserRetrieveUpdateView(RetrieveAPIView):
    """
    delete:
    Return the user with the given id.
    Requires Bearer token authentication.

    put:
    Update the user with the given id.
    Requires Bearer token authentication.
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        """
        Process the PUT HTTP method.

        Update the user instance with given id and data to update.
        Send an event about user updating to all connected Socket.io clients.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        sio.emit('update', serializer.data)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
