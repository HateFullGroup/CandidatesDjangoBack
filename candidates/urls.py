from django.urls import path

from candidates.views import TechnologiesListView, TechnologyDetail, CandidatesListView, CandidateDetail

urlpatterns = [
    path('candidates/', CandidatesListView.as_view(), name='candidates'),
    path('candidate/<int:pk>/', CandidateDetail.as_view(), name='candidate_detail'),
    path('candidate/', CandidateDetail.as_view(), name='add_candidate'),
    path('technologies/', TechnologiesListView.as_view(), name='technologies'),
    path('technology/', TechnologyDetail.as_view(), name='add_technology'),
    path('technology/<int:pk>/', TechnologyDetail.as_view(), name='technology_detail'),
]