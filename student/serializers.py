from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    student_id = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    marks = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=100)
    )

    percentage = serializers.FloatField()

    rank = serializers.IntegerField()