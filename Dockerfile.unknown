FROM python:3.12

ENV VIRTUAL_ENV=/usr/local
WORKDIR /app
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
COPY requirements.txt requirements.txt

RUN /root/.cargo/bin/uv pip install -r requirements.txt

COPY app.py app.py

CMD [ "python", "app.py" ]