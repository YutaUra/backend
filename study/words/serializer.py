from rest_framework import serializers
from study.models import Word
from study.words.session import WordPractice


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class WordPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPractice
        fields = (
            'sub_session',
            'user',
            'word',
            'answer',
        )

    @staticmethod
    def bulk_create(*validated_data):
        objs = [WordPractice(data) for data in validated_data]
        WordPractice.objects.bulk_create(objs)
