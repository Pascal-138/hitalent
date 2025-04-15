# Table Reservations

## Описание проекта
**Table Reservations** — веб-приложение - система, упрощающая бронирование столиков в ресторане. Здесь можно:
- Создавать бронь
- Просматривать бронь
- Удалять бронь
- Управлять столиками
- Управлять временнными слотами

## Стек технологий
- **Python** — основной язык программирования
- **FastAPI** — фреймворк для веб-разработки
- **PostgreSQL** — база данных для хранения данных проекта
- **SQLAlchemy** — работа с БД
- **Alembic** — для миграций
- **Markdown** — для оформления документации


## Запуск проекта в dev-режиме
1. Склонируйте репозиторий:
    ```bash
    git clone git@github.com:Pascal-138/hitalent.git
    ```
2. Запустите контейнеры:
    ```bash
    docker-compose up --build
    ```
3. Создайте и примените миграции:
    ```bash
    alembic revision --autogenerate -m "create tables"
    alembic upgrade head
    ```

## Автор
**Сидоров Алексей**  
Telegram: [@pascal161](https://t.me/pascal161)  
Email: [aleksid92@gmail.com](mailto:aleksid92@gmail.com)