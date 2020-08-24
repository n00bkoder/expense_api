from .models import Entry
from rest_framework.viewsets import ModelViewSet
from .serializers import EntrySerializer, UserSerializer
from accounts.models import User
from rest_framework import generics
from rest_framework import permissions


from rest_framework.permissions import IsAuthenticated

class EntryView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]

    queryset = Entry.objects.all()
    serializer_class = EntrySerializer



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

        







