from rest_framework import serializers
from study.models import Word, TextbookWord
from study.words.models import Mode
from study.words.session import WordPractice


class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class TextbookWordSerializer(serializers.ModelSerializer):
    word = WordSerializer(read_only=True)

    class Meta:
        model = TextbookWord
        fields = (
            'textbook_unit',
            'textbook_chapter',
            'word',
        )


class WordPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPractice
        fields = (
            'mode',
            'sub_session',
            'user',
            'word',
            'answer',
        )

    @staticmethod
    def bulk_create(*validated_data):
        objs = [WordPractice(data) for data in validated_data]
        WordPractice.objects.bulk_create(objs)
