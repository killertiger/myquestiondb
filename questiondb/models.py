from django.db import models


# Create your models here.
# TODO: explanation, tags, source, shared_text, imagedb, classification, degree
from django.utils.html import strip_tags


class QuestionType:
    Text = 't'
    MultipleChoice = 'm'


class DegreeOfDificulty:
    VeryEasy = 1,
    Easy = 2,
    Normal = 3,
    Hard = 4,
    VeryHard = 5


class Question(models.Model):
    title = models.CharField(max_length=300)
    body_html = models.TextField(verbose_name='Text')
    body_plain_text = models.TextField()
    category = models.ForeignKey("category", default=None, blank=True, null=True)

    QUESTION_TYPE = (
        ('t', 'text'),
         ('m', 'multiple choice'),
    )

    DEGREE_OF_DIFICULTY = (
        (1, 'Very Easy'),
        (2, 'Easy'),
        (3, 'Normal'),
        (4, 'Hard'),
        (5, 'Very Hard')
    )

    question_type = models.CharField(max_length=1, choices=QUESTION_TYPE, blank=False, default='t')
    degree_of_dificulty = models.IntegerField(choices=DEGREE_OF_DIFICULTY, blank=False, default=DegreeOfDificulty.Normal)

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


class Category(models.Model):
    parent = models.ForeignKey("category", default=None, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        if self.parent is not None:
            return '%s -> %s' % (self.parent, self.name)
            # return self.parent + " -> " + self.name
        return self.name

    @property
    def children(self):
        return Category.objects.filter(parent=self.pk)