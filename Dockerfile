FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# 🔥 THIS LINE MAKES openenv-server WORK
RUN pip install .

ENV PYTHONPATH=/app

CMD ["python", "server/app.py"]