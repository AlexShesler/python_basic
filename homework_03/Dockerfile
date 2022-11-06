FROM python:3.9-buster

WORKDIR /var/app

RUN pip install --upgrade pip &&  \
    pip install poetry==1.2.2

COPY poetry.lock pyproject.toml requirements.txt ./

#RUN poetry install --only main
RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0
