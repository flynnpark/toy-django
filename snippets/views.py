import re

from django.http.response import Http404
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
