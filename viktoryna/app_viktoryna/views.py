from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Question, Answer
from .forms import QuizForm, QuestionForm, AnswerForm
from django.forms import formset_factory

def home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'app_viktoryna/home.html', {'quizzes': quizzes})

def register(request):
    return render(request, 'app_viktoryna/register.html')

def quiz_view(request):
    return render(request, 'app_viktoryna/home.html')

def create_quiz(request):
    QuizFormSet = formset_factory(QuestionForm, extra=1)
    AnswerFormSet = formset_factory(AnswerForm, extra=4)

    if request.method == "POST":
        quiz_form = QuizForm(request.POST)
        question_formset = QuizFormSet(request.POST, prefix='questions')
        answer_formset = AnswerFormSet(request.POST, prefix='answers')

        if quiz_form.is_valid() and question_formset.is_valid() and answer_formset.is_valid():
            quiz = quiz_form.save()
            for question_form in question_formset:
                if question_form.cleaned_data:
                    question = question_form.save(commit=False)
                    question.quiz = quiz
                    question.save()
                    
                    for answer_form in answer_formset:
                        if answer_form.cleaned_data:
                            answer = answer_form.save(commit=False)
                            answer.question = question
                            answer.save()
            
            return redirect('home')

    else:
        quiz_form = QuizForm()
        question_formset = QuizFormSet(prefix='questions')
        answer_formset = AnswerFormSet(prefix='answers')

    return render(request, 'app_viktoryna/create_quiz.html', {
        'quiz_form': quiz_form,
        'question_formset': question_formset,
        'answer_formset': answer_formset
    })


def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('add_answer', question_id=question.id)
    else:
        form = QuestionForm()
    return render(request, 'app_viktoryna/add_question.html', {'form': form, 'quiz': quiz})

def add_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('add_answer', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'app_viktoryna/add_answer.html', {'form': form, 'question': question})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'app_viktoryna/quiz_detail.html', {'quiz': quiz, 'questions': questions})




# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.contrib.auth import logout
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Quiz
# from django.shortcuts import render, get_object_or_404, redirect
# # from .models import Question
# from .forms import QuestionForm
# from .models import Question, Answer
# from .models import Quiz


# def home(request):
#     quizzes = Quiz.objects.all()
#     return render(request, 'app_viktoryna/home.html', {
#         'quizzes': quizzes,
#     })

# def quiz_view(request):
#     question = Question.objects.first()  # для простоти беремо перше питання
#     answers = Answer.objects.filter(question=question)
#     return render(request, 'quiz.html', {'question': question, 'answers': answers})

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Реєстрація успішна! Ви можете увійти.')
#             return redirect('login')  # Перенаправлення на сторінку входу
#     else:
#         form = UserCreationForm()
#     return render(request, 'app_viktoryna/register.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return redirect('home')  # Повертаємося на домашню сторінку після виходу

# # def home(request):
# #     return render(request, 'app_viktoryna/home.html')

# @login_required
# def create_quiz(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         if title:  # Перевіряємо, що поле "Назва" заповнене
#             Quiz.objects.create(title=title, description=description)
#             return redirect('home')  # Повертаємося на головну сторінку
#     return render(request, 'app_viktoryna/create_quiz.html')



# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'app_viktoryna/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'app_viktoryna/login.html', {'form': form})

# def edit_question(request, quiz_id, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     if request.method == "POST":
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             form.save()
#             return redirect('quiz_detail', quiz_id=quiz_id)  # Повертає на сторінку вікторини
#     else:
#         form = QuestionForm(instance=question)

#     return render(request, 'app_viktoryna/edit_question.html', {'form': form, 'question': question})

# def quiz_detail(request, pk):
#     quiz = get_object_or_404(Quiz, pk=pk)
#     return render(request, 'app_viktoryna/quiz_detail.html', {'quiz': quiz})

