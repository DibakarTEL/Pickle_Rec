FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /movie/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./movie /movie/app