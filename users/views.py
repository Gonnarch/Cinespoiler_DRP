from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() # que datos usar
    serializer_class = UserSerializer # cómo transformarlos