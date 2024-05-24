from rest_framework import serializers

class ProcessPaymentSerializer(serializers.Serializer):
    current_date = serializers.DateField()
    interest_rate = serializers.FloatField()
    commercial_year_days = serializers.IntegerField()


