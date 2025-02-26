from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('subjects/', views.SubjectSelectionView.as_view(), name='subject_selection'),
    path('results/', views.ResultsView.as_view(), name='result_view'),
    #path('courses/',views.RecommendedViews.as_view(),name='recommended_courses'),
]