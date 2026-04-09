FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# 🔥 MOST IMPORTANT LINE
RUN pip install .

ENV PYTHONPATH=/app

CMD ["python", "server/app.py"]
