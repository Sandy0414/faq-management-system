from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):    
    translated_question = serializers.SerializerMethodField()
    def get_translated_question(self, obj):
        lang = self.context["request"].Get.get("lang","en")
        return obj.get_translation(lang)
    class Meta:
        model = FAQ
        fields = ['id','translated_question','answer','created_at']
