from .models import Entry
from rest_framework.viewsets import ModelViewSet
from .serializers import EntrySerializer


from rest_framework.permissions import IsAuthenticated

class EntryViewSet(ModelViewSet):
    
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    

        







