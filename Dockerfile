FROM python:3.8.5-alpine3.12

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code"

ENTRYPOINT ["python"]