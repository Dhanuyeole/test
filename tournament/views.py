from django.shortcuts import get_object_or_404, render, Http404
from django.views import View
from rest_framework.response import Response
from .models import Team, TeamMatch
from .serializers import TeamSerializer, TeamMatchSerializer, MatchSerializer
from rest_framework import generics
from rest_framework.views import APIView

class TeamSummaryView(View):
    def get(self, request, *args, **kwargs):
        team_summary = []
        teams = Team.objects.all()

        for team in teams:
            summary = {
                "team": team.country,
                "matches": team.matches_played(),
                "won": team.matches_won(),
                "lost": team.matches_lost(),
                "points": team.calculate_points(),  # You need to implement this method
            }
            team_summary.append(summary)

        return render(request, 'team_list.html', {'team_summary': team_summary})

class TeamMatchesView(View):
    # template_name = 

    def get(self, request, team_name, *args, **kwargs):
        team = Team.objects.get(pk=team_name)
        team_matches = TeamMatch.objects.filter(team=team)
    
        return render(request, 'team_view.html', {'team': team, 'team_matches': team_matches})
    
class TeamListView(APIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailView(APIView):
    def get(self, request, team_name, format=None):
        team = get_object_or_404(Team, pk=team_name)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    
class TeamMatchesListView(APIView):
    def get(self, request, *args, **kwargs):
        team_matches = TeamMatch.objects.all()
        serializer = TeamMatchSerializer(team_matches, many=True)
        return Response(serializer.data)