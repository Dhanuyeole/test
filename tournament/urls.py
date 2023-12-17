from django.urls import path
from .views import TeamSummaryView, TeamMatchesView, TeamListView, TeamDetailView, TeamMatchesListView

urlpatterns = [
    path('team/', TeamSummaryView.as_view(), name='team'),
    path('tournament/team/<str:team_name>/', TeamMatchesView.as_view(), name='team'),
    path('v1/teams/', TeamListView.as_view(), name='team-list'),
    path('v1/teams/<str:team_name>/', TeamDetailView.as_view(), name='team-details'),
    path('v1/teams/matches/', TeamMatchesListView.as_view(), name='all-teams-matches-list'),




    
]