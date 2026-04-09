FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

CMD ["python", "server/app.py"]