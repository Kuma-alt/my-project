from django import forms
from .models import Quiz, Question, Answer

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']





# from django import forms
# from .models import Question, Answer
# from django.shortcuts import render, redirect
# from .models import Quiz, Question

# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['question_type', 'question_text', 'image', 'video_url']  

# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ['question', 'is_correct']  


# def edit_question(request, quiz_id, question_id=None):
#     quiz = Quiz.objects.get(id=quiz_id)
#     if question_id:
#         question = Question.objects.get(id=question_id)
#     else:
#         question = None

#     if request.method == 'POST':
#         question_form = QuestionForm(request.POST, request.FILES, instance=question)
#         answer_forms = [AnswerForm(request.POST, instance=ans) for ans in question.answers.all()]
        
#         if question_form.is_valid():
#             question = question_form.save(commit=False)
#             question.quiz = quiz
#             question.save()

#             for form in answer_forms:
#                 if form.is_valid():
#                     form.save()

#             return redirect('quiz_detail', quiz_id=quiz.id)
#     else:
#         question_form = QuestionForm(instance=question)
#         answer_forms = [AnswerForm(instance=ans) for ans in question.answers.all()]

#     return render(request, 'app_viktoryna/edit_question.html', {
#         'quiz': quiz,
#         'question_form': question_form,
#         'answer_forms': answer_forms,
#     })


