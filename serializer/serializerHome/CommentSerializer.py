from rest_framework import serializers
from .models import Comment
class CommentSerializerIn(serializers.Serializer):
        class Meta:
            model = Comment
            fields = ['name', 'login', 'password', 'email']


class CommentSerializerInOut(serializers.Serializer):
    class Meta:
        model = Comment
        fields = ['id','name', 'login', 'password', 'email']