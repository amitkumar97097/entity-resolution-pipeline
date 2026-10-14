# lightweight base python use template
FROM python:3.10-slim

WORKDIR /app

# update requirements and packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# project modules move inside docker image file-system 
COPY src/ ./src/
COPY data/ ./data/
COPY app.py .
COPY main.py .

EXPOSE 8000

# API auto-serve triggers
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]