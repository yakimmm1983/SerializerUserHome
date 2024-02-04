from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .CommentSerializer import CommentSerializerIn,CommentSerializerInOut
from .models import Comment

@api_view(['POST'])
def userIn (request):
    if request.method == "POST":
        comment = Comment(**CommentSerializerIn(data = JSONParser().parse(io.BytesIO(request.body))))
        return Response(comment) #status????

@api_view(['POST'])
def userOut (request):
    comment = Comment.objects.get()
    serializer = CommentSerializerInOut(comment)
    json = JSONRenderer().render(serializer.data)
    return Response(json)

