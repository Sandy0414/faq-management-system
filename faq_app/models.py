from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextUploadingField()

    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_translation(self, lang):
        translations = {
            "hi": self.question_hi,
            "bn": self. question_bn
            }
        return translations.get(lang,self.question)
    def __str__(self):
        return self.question
