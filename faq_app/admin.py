from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget 
from .models import FAQ


class FAQAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget(config_name='default'))  

    class Meta:
        model = FAQ
        fields = "__all__"


class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm


admin.site.register(FAQ, FAQAdmin)
