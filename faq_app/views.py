from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from googletrans import Translator
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        cache_key = f"faqs_{request.GET.get('lang', 'en')}"
        cache_data = cache.get(cache_key)

        if cache_data: 
            return Response(cache_data)

        faqs = self.get_queryset()
        serializer = self.get_serializer(faqs, many=True)

        cache.set(cache_key, serializer.data, timeout=3600)  
        return Response(serializer.data)

    def perform_create(self, serializer):
        instance = serializer.save()
        translator = Translator()

        try:
            if not instance.question_hi:
                instance.question_hi = translator.translate(instance.question, dest="hi").text
            if not instance.question_bn:
                instance.question_bn = translator.translate(instance.question, dest="bn").text
        except Exception as e:
            print(f"Translation failed: {e}")  

        instance.save()
