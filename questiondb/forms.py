from django.forms import ModelForm, inlineformset_factory

from questiondb.models import Question, Alternative


class AlternativeForm(ModelForm):
    class Meta:
        model = Alternative
        exclude = ['body_plain_text',]

AlternativeFormSet = inlineformset_factory(Question, Alternative, form=AlternativeForm, extra=1)