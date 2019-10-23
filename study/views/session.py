from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(http_method_names=('GET',))
@permission_classes(permission_classes=(IsAuthenticated,))
def get_word_session(request):
    user = request.user
    sessions = user.studysession_set.order_by('-created_at')[:5]
    data = []
    for session in sessions:
        for ws in session.wordsession_set.all():
            wp = ws.wordpractice_set.all()
            correct = wp.filter(word=F('answer'))
            data.append(dict(
                correct=len(correct),
                answer=len(wp),
                datetime=ws.updated_at.astimezone(tz=None),
            ))
    return Response(data, status=HTTP_200_OK)
