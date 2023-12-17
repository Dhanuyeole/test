from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

    total_matches_played = models.IntegerField(default=0)
    total_matches_won = models.IntegerField(default=0)
    total_matches_lost = models.IntegerField(default=0)


    def matches_played(self):
        return self.total_matches_played

    def matches_won(self):
        return self.total_matches_won

    def matches_lost(self):
        return self.total_matches_lost

    def calculate_points(self):
        # You can adjust this based on your scoring system
        return self.matches_won() * 2
    
class Match(models.Model):
    date = models.DateField()

class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()
    won = models.BooleanField(default=False)  # Add this line