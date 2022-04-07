from django.urls import path

from applications.blog.views import NewsView

urlpatterns = [
    path('', NewsView.as_view()),
]
