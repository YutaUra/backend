from rest_framework import serializers
from study.models import Word, WordHistory


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class WordHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WordHistory
        fields = (
            'user',
            'word',
            'answer',
        )
