"""
URLs for courses_list.
"""
from django.urls import path, re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from courses_list.views.list import CourseListView

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="courses_list/base.html")),
    path(r'/list/', CourseListView.as_view())
]
