# quiz/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import QuizQuestion

def quiz_view(request):
    if request.method == 'POST':
        score = 0
        questions = QuizQuestion.objects.all()
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_option:
                score += 1
        return render(request, 'pages/result.html', {'score': score})
    else:
        questions = QuizQuestion.objects.all()
        return render(request, 'pages/quiz.html', {'questions': questions})
