FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

EXPOSE 50000
CMD ["gunicorn", "-b", "0.0.0.0:50000", "app:app"]

