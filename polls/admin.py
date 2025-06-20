from django.contrib import admin

from .models import Choice, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
