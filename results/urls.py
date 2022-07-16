from django.urls import path
from .views import (ResultsList, UserResults, ResultDetails, ResultCreate)

urlpatterns = [
    # All results for admin only
    path('results/', ResultsList.as_view(), name='results_list'),

    path('user-results/', UserResults.as_view(),
         name='user_results'),  # User results
    path('results/<int:pk>/', ResultDetails.as_view(),
         name='result_details'),  # Individual result
    path('result-create/',
         ResultCreate.as_view(), name='result_create'),  # To create a new user result
]
