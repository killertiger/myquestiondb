from django.db import models


# Create your models here.
# TODO: explanation, tags, source, shared_text, imagedb, classification
class Question(models.Model):
    title = models.CharField(max_length=300)
    body_html = models.TextField()
    body_plain_text = models.TextField()

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey("question")
    body_html = models.TextField()
    body_plain_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.body_plain_text
