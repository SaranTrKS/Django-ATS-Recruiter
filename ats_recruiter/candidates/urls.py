from django.urls import path
from . import views

urlpatterns = [
    path('candidates/', views.candidate_list, name='candidate-list'),
    path('candidates/search/', views.search_candidates, name='candidate-search'),
    path('candidates/<int:pk>/', views.candidate_detail, name='candidate-detail'),
]

# urlpatterns = [
#     path('candidates/', views_2.get_candidates, name='get_candidates'),
#     path('candidates/<int:pk>/', views_2.get_candidate, name='get_candidate'),
#     path('candidates/create/', views_2.create_candidate, name='create_candidate'),
#     path('candidates/update/<int:pk>/', views_2.update_candidate, name='update_candidate'),
#     path('candidates/delete/<int:pk>/', views_2.delete_candidate, name='delete_candidate'),
# ]