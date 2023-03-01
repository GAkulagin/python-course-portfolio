from django.urls import path

from jobs.views import IndexJobsDetailView, IndexJobsListView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", IndexJobsDetailView.as_view(), name="job"),
]