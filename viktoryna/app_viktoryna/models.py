from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text





# # from django.db import models

# # class Quiz(models.Model):
# #     title = models.CharField(max_length=200)
# #     description = models.TextField()

# # class Question(models.Model):
# #     TEXT = 'text'
# #     IMAGE = 'image'
# #     VIDEO = 'video'
# #     QUESTION_TYPES = [
# #         (TEXT, 'Текстове питання'),
# #         (IMAGE, 'Питання із зображенням'),
# #         (VIDEO, 'Питання з відео'),
# #     ]

# #     quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
# #     question_text = models.CharField(max_length=255)
# #     question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default=TEXT)
# #     time_limit = models.IntegerField(default=30)  # Час на відповідь в секундах
# #     image = models.ImageField(upload_to='question_images/', null=True, blank=True)
# #     video_url = models.URLField(null=True, blank=True)
    
# #     def __str__(self):
# #         return self.question_text

# # class Answer(models.Model):
# #     question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
# #     answer_text = models.CharField(max_length=255)
# #     is_correct = models.BooleanField(default=False)

# #     def __str__(self):
# #         return self.answer_text


# from django.db import models
# from django.utils import timezone

# class Quiz(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# QUESTION_TYPE_CHOICES = [
#     ('multiple_choice', 'Multiple Choice'),
#     ('true_false', 'True/False'),
# ]

# class Question(models.Model):
#     question_text = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='questions/images/', null=True, blank=True)
#     video_url = models.URLField(null=True, blank=True)
#     time_limit = models.IntegerField(default=30)
#     question_type = models.CharField(max_length=50, choices=QUESTION_TYPE_CHOICES)



# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer_text = models.CharField(max_length=255)  
#     is_correct = models.BooleanField(default=False)


#     def __str__(self):
#         return self.text
