from django.urls import path
from . import views

# urlpatterns = [
# #     #path('candidates/search/', views.candidate_search, name='candidate-search'),
# #     path('candidates/', views_1.candidate_list, name='candidate-list'),
# #     path('candidates/<int:pk>/', views_1.candidate_detail, name='candidate-detail'),


# ]

urlpatterns = [
    path('candidates/', views.get_candidates, name='get_candidates'),
    path('candidates/<int:pk>/', views.get_candidate, name='get_candidate'),
    path('candidates/create/', views.create_candidate, name='create_candidate'),
    path('candidates/update/<int:pk>/', views.update_candidate, name='update_candidate'),
    path('candidates/delete/<int:pk>/', views.delete_candidate, name='delete_candidate'),
]