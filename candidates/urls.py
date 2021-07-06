from django.urls import path

from candidates.views import TechnologiesListView, TechnologyView, TechnologyDetail

urlpatterns = [
    path('technologies/', TechnologiesListView.as_view(), name='technologies'),
    # path('technologies/', TechnologyView.as_view(), name='technologies'),
    path('technology/<int:pk>/', TechnologyDetail.as_view(), name='technologies'),
]