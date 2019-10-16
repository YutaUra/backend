from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from study.words.serializer import WordSerializer, WordHistorySerializer
from study.models import Word
from uuid import UUID
from users.models import User


class WordGetView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        subject = self.kwargs.get('subject')
        if subject == 'english':
            query_set = Word.objects.filter(subject__name='英語')
        elif subject == 'math':
            query_set = Word.objects.filter(subject__name='数学')
        else:
            return

        textbook_name = self.kwargs.get('textbook_name')
        query_set = query_set.filter(textbook_unit__textbook__name=textbook_name)

        unit_name = self.kwargs.get('unit_name')
        if unit_name:
            query_set = query_set.filter(textbook_unit__name=unit_name)
            chapter_name = self.kwargs.get('chapter_name')
            if chapter_name:
                query_set = query_set.filter(textbook_chapter__name=chapter_name)

        return query_set


class WordAnswerView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = WordHistorySerializer

    def save_serializers(self, *serializers):
        for serializer in serializers:
            serializer.save()

    def create_data(self, data):
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer

    def get_user_id(self, string):
        try:
            UUID(string)
        except ValueError:
            # uuidではない➡通常のid
            try:
                user = User.objects.get(pub_id=string)
            except User.DoesNotExist:
                return None
            return user.user_id
        return string

    def create(self, request, *args, **kwargs):
        """複数のデータから一括で作成する"""
        data = request.data
        if isinstance(data, list):
            """複数データ"""
            serializers = []
            for d in data:
                d['user'] = self.get_user_id(d['user'])
                serializers.append(self.create_data(d))
            self.save_serializers(*serializers)
        elif isinstance(data, dict):
            """一つのデータ"""
            data['user'] = self.get_user_id(data['user'])
            serializer = self.create_data(data)
            self.save_serializers(serializer)
        return Response(status=status.HTTP_201_CREATED)