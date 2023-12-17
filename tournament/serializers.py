from rest_framework import serializers
from .models import Team, Match, TeamMatch

class TeamSerializer(serializers.ModelSerializer):
    matches_played = serializers.SerializerMethodField()
    matches_won = serializers.SerializerMethodField()
    matches_lost = serializers.SerializerMethodField()
    calculate_points = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    def get_matches_played(self, obj):
        return obj.matches_played()

    def get_matches_won(self, obj):
        return obj.matches_won()

    def get_matches_lost(self, obj):
        return obj.matches_lost()

    def get_calculate_points(self, obj):
        return obj.calculate_points()

    
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class TeamMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMatch
        fields = '__all__'