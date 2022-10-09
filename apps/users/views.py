from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.order_by('id')
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserUpdateView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)






