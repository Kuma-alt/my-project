from django.contrib import admin
from django.urls import path
from app_viktoryna import views  
from .views import create_quiz

urlpatterns = [
    # path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/add_question/', views.add_question, name='add_question'),
    path('question/<int:question_id>/add_answer/', views.add_answer, name='add_answer'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]


# from django.urls import path
# from . import views
# from .views import quiz_detail

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('create-quiz/', views.create_quiz, name='create_quiz'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('register/', views.register_view, name='register'),
#     path('quiz/<int:quiz_id>/edit_question/<int:question_id>/', views.edit_question, name='edit_question'),
#     path('quiz/<int:quiz_id>/create_question/', views.edit_question, name='create_question'),
#     path('quiz/<int:pk>/', quiz_detail, name='quiz_detail'),
# ]



