from rest_framework import serializers
from study.models import Textbook, TextbookUnit, TextbookChapter


class TextbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook
        fields = '__all__'


class TextbookUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextbookUnit
        fields = '__all__'


class TextbookChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextbookChapter
        fields = '__all__'
