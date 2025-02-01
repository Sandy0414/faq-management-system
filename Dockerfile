FROM python:3.11
# Set working directory  in container
WORKDIR /app
#Copy project files
COPY . /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
