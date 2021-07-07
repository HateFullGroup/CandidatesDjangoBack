from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from candidates.models import Technology, Candidate
from candidates.serializers import TechnologySerializer, CandidateDetailSerializer


class TechnologiesListView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    pagination_class = LimitOffsetPagination

    #
    # def get(self, request, *args, **kwargs):
    #     queryset = Technology.objects.all()
    #     serializer = TechnologySerializer(queryset, many=True)
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)


# class TechnologyView(APIView):
#     # permission_classes = (IsAuthenticated,)
#     def post(self, request):
#         name = request.data.get('name')
#         # Create an article from the above data
#         serializer = TechnologySerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             technology_saved = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class TechnologyDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Technology
    serializer_class = TechnologySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            technology_saved = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Candidate
#     serializer_class = TechnologySerializer

class CandidatesListView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = Candidate.objects.all()
    serializer_class = CandidateDetailSerializer
    pagination_class = LimitOffsetPagination


class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Candidate
    serializer_class = CandidateDetailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            candidate_saved = serializer.save()
            return Response(candidate_saved, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)