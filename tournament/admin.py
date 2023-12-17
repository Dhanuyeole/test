# In your admin.py file


from django.contrib import admin
from .models import Team, Match, TeamMatch

class TeamAdmin(admin.ModelAdmin):
    list_display = ('country', 'total_matches_played', 'total_matches_won', 'total_matches_lost')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('date',)

class TeamMatchAdmin(admin.ModelAdmin):
    list_display = ('team', 'match', 'batting_score', 'batting_wickets', 'batting_overs', 'won')

admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(TeamMatch, TeamMatchAdmin)


