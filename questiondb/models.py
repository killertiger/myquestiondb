from django.db import models


# Create your models here.
# TODO: explanation, tags, source, shared_text, imagedb, classification, question type
from django.utils.html import strip_tags


class Question(models.Model):
    title = models.CharField(max_length=300)
    body_html = models.TextField(verbose_name='Text')
    body_plain_text = models.TextField()

    QUESTION_TYPE = (
        (('t', 'text'),
         ('m', 'multiple choice')),
    )

    question_type = models.CharField(max_length=1, choices=QUESTION_TYPE, blank=False, default='t')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.body_plain_text = strip_tags(self.body_html)
        super(Question, self).save()


class Alternative(models.Model):
    question = models.ForeignKey("question")
    body_html = models.TextField()
    body_plain_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.body_plain_text


class QuestionType:
    Text = 't'
    MultipleChoice = 'm'
