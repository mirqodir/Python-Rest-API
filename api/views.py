from rest_framework.generics import ListCreateAPIView  ,RetrieveUpdateDestroyAPIView
from my_app.models import User,Client
from .serializers import UserSeralizers,ClientSeralizers
from rest_framework import permissions





# userslar uchun
class UserView(ListCreateAPIView ):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class  = UserSeralizers


class UserDetail(RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class  = UserSeralizers


# clientlar uchun
class ClientView(ListCreateAPIView ):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Client.objects.all()
	serializer_class  = ClientSeralizers



class ClientDetail(RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Client.objects.all()
	serializer_class  = ClientSeralizers