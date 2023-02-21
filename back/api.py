from back.models import UserProfile, Post, Comment
from rest_framework import viewsets, permissions
from .serializers import UserSerializers, PostSerializers, CommentSerializers
from rest_framework.response import Response

# Viewset
class UserViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = UserProfile.objects.all()
        permission_classes = [
            permissions.AllowAny
        ]
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)