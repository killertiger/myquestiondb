from django.forms import ModelForm, inlineformset_factory

from questiondb.models import Question, Alternative


class AlternativeForm(ModelForm):
    class Meta:
        model = Alternative
        fields = ['is_correct', 'body_html', ]

AlternativeFormSetCreate = inlineformset_factory(Question, Alternative, form=AlternativeForm, extra=4)
AlternativeFormSetUpdate = inlineformset_factory(Question, Alternative, form=AlternativeForm, extra=0)