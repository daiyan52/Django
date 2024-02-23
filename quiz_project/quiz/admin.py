from django.contrib import admin
from .models import QuizQuestion

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option1', 'option2', 'option3', 'option4', 'correct_option')

admin.site.register(QuizQuestion, QuizQuestionAdmin)
