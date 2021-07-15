from django.urls.conf import path

from polls import views

urlpatterns = [
    path('questions', views.QuestionList.as_view()),
    path('questions/<int:pk>', views.QuestionDetail.as_view()),
]
