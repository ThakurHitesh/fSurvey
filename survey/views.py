from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Choice
from .serializers import QuestionListPageSerializer, QuestionDetailPageSerializer, ChoiceSerializer


class QuestionsAPIView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            question = get_object_or_404(Question, pk=pk)
            serializer = QuestionDetailPageSerializer(question)
        else:
            questions = Question.objects.all()
            serializer = QuestionListPageSerializer(questions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = QuestionListPageSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionListPageSerializer(question).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionDetailPageSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionDetailPageSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)


class ChoicesAPIView(APIView):
    
    def post(self, request):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        choice = Choice.objects.filter(id=pk)[0]
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            choice =serializer.save()
            return Response("Voted")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionResultAPIView(APIView):
    
    def get(self, request, pk):
        choices = Choice.objects.filter(question_id=pk).order_by('-votes')
        serializer = ChoiceSerializer(choices[0])
        return Response(serializer.data)
