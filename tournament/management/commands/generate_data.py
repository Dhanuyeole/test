# tournament/management/commands/generate_data.py

from django.core.management.base import BaseCommand
from faker import Faker
from tournament.models import Team, Match, TeamMatch

fake = Faker()

class Command(BaseCommand):
    help = 'Generate random data for teams, matches, and team matches'

    def handle(self, *args, **kwargs):
        # Create 10 teams
        teams = [self.get_or_create_team(country=fake.country_code()) for _ in range(10)]

        # Create 40 matches
        matches = [Match.objects.create(date=fake.date_this_decade()) for _ in range(40)]

        # Create team matches with random scores, wickets, and overs
        for match in matches:
            for team in teams:
                TeamMatch.objects.create(
                    team=team,
                    match=match,
                    batting_score=fake.random_int(min=50, max=300),
                    batting_wickets=fake.random_int(min=0, max=10),
                    batting_overs=fake.random_int(min=10, max=50),
                )

        self.stdout.write(self.style.SUCCESS('Data generated successfully.'))

    def get_or_create_team(self, country):
        team, created = Team.objects.get_or_create(country=country)
        return team

