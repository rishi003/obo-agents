FROM python:3.10-slim-bookworm
WORKDIR /app

RUN apt-get update && \
    apt-get install --no-install-recommends -y wget libpq-dev gcc g++ python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app
COPY main.py .
COPY cli.py .

EXPOSE 8000
CMD ["python", "cli.py"]