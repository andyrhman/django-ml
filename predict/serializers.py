from rest_framework import serializers

class PredictSerializer(serializers.Serializer):
    ProductName = serializers.CharField(max_length=255)
    Administrative = serializers.FloatField()
    Informational = serializers.FloatField()
    ProductRelated = serializers.FloatField()
    BounceRates = serializers.FloatField()
    ExitRates = serializers.FloatField()
    PageValues = serializers.FloatField()
    SpecialDay = serializers.FloatField()
    OperatingSystems = serializers.IntegerField()
    Browser = serializers.IntegerField()
    Region = serializers.IntegerField()
    TrafficType = serializers.IntegerField()
    VisitorType = serializers.IntegerField()
    Weekend = serializers.IntegerField()
