FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv sync --all-groups

RUN uv run pytest

CMD ["uv", "run", "python", "src/calculator/calculator.py"]

