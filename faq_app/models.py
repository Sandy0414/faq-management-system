from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
