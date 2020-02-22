from django.urls import path
from .views import QuestionsAPIView, ChoicesAPIView, QuestionResultAPIView

urlpatterns = [
    path('questions/', QuestionsAPIView.as_view(), name='questions_view'),
    path('questions/<slug:pk>/', QuestionsAPIView.as_view(), name='questions_view'),
    path('choices/', ChoicesAPIView.as_view(), name='choices_view'),
    path('choices/<slug:pk>/', ChoicesAPIView.as_view(), name='choice_view'),
    path('result/<slug:pk>/', QuestionResultAPIView.as_view(), name='question_result_view'),
]
