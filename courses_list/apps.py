"""
courses_list Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs
)


class CoursesListConfig(AppConfig):
    """
    Configuration for the courses_list Django application.
    """

    name = 'courses_list'
    plugin_app = {

        # Configuration setting for Plugin URLs for this app.
        PluginURLs.CONFIG: {

            # Configure the Plugin URLs for each project type, as needed.
            "lms.djangoapp": {

                # The namespace to provide to django's urls.include.
                PluginURLs.NAMESPACE: 'courses_list',

                # The application namespace to provide to django's urls.include.
                # Optional; Defaults to None.
                PluginURLs.APP_NAME: 'courses_list',

                # The regex to provide to django's urls.url.
                # Optional; Defaults to r''.
                PluginURLs.REGEX: r'api/courses_list',

                # The python path (relative to this app) to the URLs module to be plugged into the project.
                # Optional; Defaults to 'urls'.
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        },
   }