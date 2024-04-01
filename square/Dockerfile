FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

EXPOSE 50002
CMD ["gunicorn", "-b", "0.0.0.0:50002", "app:app"]
