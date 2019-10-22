from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from study.words.serializer import WordPracticeSerializer, WordSerializer
from study.words.models import Word, TextbookWord
from study.models import StudySession, WordSession, WordGet
from uuid import UUID
from users.models import User


class WordGetView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = TextbookWord.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        params = self.request.query_params.dict()
        query_set = self.queryset.filter(**params)
        return Word.objects.filter(id__in=query_set.values_list('word', flat=True))

    def list(self, request, *args, **kwargs):
        # セッションの作成
        session = StudySession.objects.create_or_get_current_session(request.user)
        sub_session = WordSession.objects.create_or_get_current_session(request.user, session=session)
        range_name = \
            str(self.kwargs.get('textbook_name')) + ' ' + \
            str(self.kwargs.get('unit_name')) + ' ' + \
            (str(self.kwargs.get('chapter_name')) if self.kwargs.get('chapter_name') else '')
        if isinstance(request.user, User):
            word_get = WordGet(user=request.user, sub_session=sub_session, get_range=range_name)
        else:
            word_get = WordGet(sub_session=sub_session, get_range=range_name)
        word_get.save()
        return super().list(request, *args, **kwargs)


class WordAnswerView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = WordPracticeSerializer

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
        # sessionの作成
        session = StudySession.objects.create_or_get_current_session(request.user)
        sub_session = WordSession.objects.create_or_get_current_session(request.user, session=session)
        data = request.data
        if isinstance(data, list):
            """複数データ"""
            serializers = []
            for d in data:
                d['user'] = self.get_user_id(d['user'])
                d['sub_session'] = sub_session.pk
                serializers.append(self.create_data(d))
            self.save_serializers(*serializers)
        elif isinstance(data, dict):
            """一つのデータ"""
            data['user'] = self.get_user_id(data['user'])
            data['sub_session'] = sub_session.pk
            serializer = self.create_data(data)
            self.save_serializers(serializer)

        return Response(status=status.HTTP_201_CREATED)
