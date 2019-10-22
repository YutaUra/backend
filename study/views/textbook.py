"""教科書に対応するユニット等を取り出すビュー"""
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from study.serializer.textbook import TextbookSerializer, TextbookUnitSerializer, TextbookChapterSerializer
from study.models import Textbook, TextbookUnit, TextbookChapter


class TextbookGetView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer

    def get_queryset(self):
        subject = self.kwargs.get('subject')
        if subject == 'english':
            query_set = self.queryset.filter(subject__name='英語')
        elif subject == 'math':
            query_set = self.queryset.filter(subject__name='数学')
        else:
            return
        return query_set


class TextbookUnitGetView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = TextbookUnit.objects.all()
    serializer_class = TextbookUnitSerializer

    def get_queryset(self):
        params = self.request.query_params.dict()
        query_set = self.queryset.filter(**params)
        return query_set


class TextbookChapterGetView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = TextbookChapter.objects.all()
    serializer_class = TextbookChapterSerializer

    def get_queryset(self):
        params = self.request.query_params.dict()
        query_set = self.queryset.filter(**params)
        return query_set
