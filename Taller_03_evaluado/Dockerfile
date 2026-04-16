FROM python:3.12-slim

WORKDIR /app

COPY ./docker_with_problems/src/requirements.txt .

RUN pip install --no-cache-dir uv

RUN uv venv && uv pip install -r requirements.txt

COPY /docker_with_problems/src/app.py .

CMD ["uv", "run", "python", "app.py"]
