from django.urls import path

from candidates.views import TechnologiesListView, TechnologyDetail, CandidatesListView

urlpatterns = [
    path('candidates/', CandidatesListView.as_view(), name='candidates'),
    path('technologies/', TechnologiesListView.as_view(), name='technologies'),
    path('technology/', TechnologyDetail.as_view()),
    # path('technologies/', TechnologyView.as_view(), name='technologies'),
    path('technology/<int:pk>/', TechnologyDetail.as_view(), name='technology'),
]