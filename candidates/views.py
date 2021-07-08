from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from candidates.models import Technology, Candidate
from candidates.serializers import TechnologySerializer, CandidateDetailSerializer, CandidateTechnologySerializer


class TechnologiesListView(ListAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TechnologiesListView, self).dispatch(request, *args, **kwargs)
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
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TechnologyDetail, self).dispatch(request, *args, **kwargs)
    # permission_classes = (IsAuthenticated,)
    queryset = Technology
    serializer_class = TechnologySerializer
    # def get(self):
    #     breakpoint()

    def get(self, request, *args, **kwargs):
        # breakpoint()
        return self.retrieve(request, *args, **kwargs)


    def post(self, request):
        # breakpoint()
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
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CandidatesListView, self).dispatch(request, *args, **kwargs)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)
    queryset = Candidate.objects.all()
    serializer_class = CandidateDetailSerializer
    pagination_class = LimitOffsetPagination


class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CandidateDetail, self).dispatch(request, *args, **kwargs)
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

    def put(self, request, *args, **kwargs):
        try:
            candidate = Candidate.objects.get(pk=kwargs['pk'])
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(candidate, data=request.data,
                                           context={"candidate_id": kwargs['pk']})
        if serializer.is_valid(raise_exception=True):
            # ct_serializer = CandidateTechnologySerializer(data=candidatetechnology_set, context=self.context)
            candidate_saved = serializer.save()
            # candidate_saved = 'xd'
            return Response(candidate_saved, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    def delete(self, request, pk):
        try:
            candidate = Candidate.objects.get(pk=pk)
        except Candidate.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        candidate.candidatetechnology_set.all().delete()
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)