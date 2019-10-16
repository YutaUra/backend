from django import forms
from study.models import Unit


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Unit.objects.filter(
            subject__id=self.instance.subject_id
        ).exclude(pk=self.instance.pk)
