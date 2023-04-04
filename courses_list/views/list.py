from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


def get_param(params, key, data_type, default=None):
    try:
        return data_type(params.get(key)) if params.get(key) else default
    except ValueError:
        raise ParseError


class CourseListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = CourseOverview.objects.all()

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        title = get_param(request.query_params, "title", str)
        if title:
            qs = qs.filter(display_name=title)
        language = get_param(request.query_params, "language", str)
        if language:
            qs = qs.filter(language=language)
        return Response(list(qs.values('display_name', 'language')), status=200)
