FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY backend ./backend
COPY knowledge-base ./knowledge-base
COPY analytics ./analytics

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Use $PORT when the hosting platform provides one (e.g. Render), otherwise
# default to 8000 for local docker-compose/App Service use.
CMD ["sh", "-c", "python -m uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}"]