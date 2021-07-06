from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from candidates.models import Technology
from candidates.serializers import TechnologySerializer


class TechnologiesListView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    pagination_class = LimitOffsetPagination


    def get(self, request, *args, **kwargs):
        print(request, args, **kwargs)

        serializer = TechnologySerializer(self.queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TechnologyView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        name = request.data.get('name')
        # Create an article from the above data
        serializer = TechnologySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            technology_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(technology_saved.title)})


class TechnologyDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Technology
    serializer_class = TechnologySerializer