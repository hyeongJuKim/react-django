from rest_framework import serializers
from .models import WiseSaying

# 직렬화
class WiseSayingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiseSaying
        fields = '__all__'