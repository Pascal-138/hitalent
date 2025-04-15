FROM python:3.12-alpine

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libpq \
    postgresql-dev \
    python3-dev \
    libffi-dev \
    build-base \
    curl

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
