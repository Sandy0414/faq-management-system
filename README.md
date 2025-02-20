## 📖Overview

A multilingual FAQ management system built with Django. The system allows the storage and management of FAQs, integrating a WYSIWYG editor for content formatting,
multilingual support with dynamic translations, and caching for optimal performance.This Django REST API provides multilingual support for frequently asked questions(FAQs)using Google
Translate.The application includes caching with Redis for optimized performance.

## 🎯 Key Features
- **FAQ Model**: Store questions and answers in multiple languages.
- **WYSIWYG Editor**: Rich text formatting support via django-ckeditor.
- **Multilingual Support**: Translations managed via Google Translate API and googletrans.
- **Caching**: Redis-powered translation caching for faster API responses.
- **REST API**: Fetch FAQs in different languages via query parameters.
- **Django Admin**: User-friendly interface to manage FAQs.
- **Testing**: Unit tests written with `pytest` to ensure code quality.


## 🛠️ Installation 
Requirements:
- Python 3.13
- Django
- django-ckeditor
- Docker & Dcker Compose
- Redis
- Google Translate API (or googletrans)

## Steps: 

1. Clone the Repository

git clone https://github.com/Sandy0414/faq-management-system.git 
```
cd faq-management-system
```
2. Create a Virtual Environment
```
python -m venv venv 
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
4. Install Dependencies
```
pip install -r requirements.txt
```
6. Run Migrations
```
python manage.py migrate
```
8. Start Redis (If running locally, install Redis and start the service)
```
redis-server
```
10. Docker Setup 
```
docker-compose up --build
```
7. Run the Development Server
```
python manage.py runserver
```
## 🌍 API Usage

Fetch FAQs by Language

English:

curl http://localhost:8000/faqs/?lang=en

Hindi:

curl http://localhost:8000/faqs/?lang=hi

Bengali:

curl http://localhost:8000/faqs/?lang=bn


Create FAQ

To create a new FAQ, use the following format for a POST request:

{
  "question": "What is Django?",
  "answer": "Django is a high-level Python web framework.",
  "question_hi": "डजैंगो क्या है?",
  "answer_hi": "डजैंगो एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।"
}

## 🧪 Testing

Unit tests are written using pytest. Run tests with the following command:

pytest


## ⚙️ Git & Version Control

Commit Guidelines

feat: Add new features.

fix: Fix bugs or issues.

docs: Update documentation.


Example Commits:

feat: Adds multilingual FAQ model
fix: Improves translation caching
docs: Update README with API examples


## 🐳 Docker Support

Steps to run in Docker:

1. Build the Docker image:

docker build -t faq-management-system .


2. Run the container:

docker run -p 8000:8000 faq-management-system


## 🚀 Deployment

You can deploy this application to platforms like Heroku or AWS. Follow their respective documentation for deployment instructions.

## 🤝 Contributing

1. Fork the repository.

2. Create a new branch: git checkout -b feature-branch.

3. Make your changes and commit: git commit -am 'Add new feature'.

4. Push your branch: git push origin feature-branch.

5. Open a Pull Request.
   

## 📜 License

This project is licensed under the MIT License.




