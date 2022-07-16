from rest_framework import serializers
from .models import Results

class ResultsSerializer(serializers.ModelSerializer):
    result_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Results
        fields = "__all__"
        
    def validate_result(self, value):
        if value>=0 and value<=3:
            return value
        else:
            raise serializers.ValidationError("result must be between 0 and 3")
