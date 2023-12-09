from django.contrib import admin
from .models import Category , Quiz , Question , Choice

# Register your models here.
@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["title"]

admin.site.register(Question)
admin.site.register(Choice)

