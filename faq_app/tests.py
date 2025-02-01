from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from faq_app.models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="What is Django?", answer="A Python framework.")
    assert faq.question == "What is Django?"

@pytest.mark.django_db
def test_api_response():
    client = APIClient()
    response = client.get("/api/faqs/")
    assert response.status_code == 200
