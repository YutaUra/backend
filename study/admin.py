from django.contrib import admin
from study.models import *
from study.forms.unit import UnitForm
from study.forms.textbook_chapter import TextbookChapterForm


class UnitAdmin(admin.ModelAdmin):
    form = UnitForm


class TextbookChapterAdmin(admin.ModelAdmin):
    form = TextbookChapterForm


admin.site.register(School)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Publisher)
admin.site.register(Textbook)
admin.site.register(TextbookUnit)
admin.site.register(TextbookChapter, TextbookChapterAdmin)
admin.site.register(Word)
