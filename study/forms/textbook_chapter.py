from django import forms
from study.models import TextbookChapter, Unit


class TextbookChapterForm(forms.ModelForm):
    class Meta:
        model = TextbookChapter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.instance.__dict__)
        self.fields['unit'].queryset = Unit.objects.filter(
            id__in=[self.instance.textbook_unit_id]
        )
