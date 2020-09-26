FROM python:3.8.5-alpine3.12

WORKDIR .

COPY . .

# These next two env vars are to make aiohttp build in a docker environment,
# there are no wheels on PyPi for alpine linux. This disables some compiling
# and has some performance implications, but should not affect the code samples
# in this book
ENV YARL_NO_EXTENSIONS 1
ENV MULTIDICT_NO_EXTENSIONS 1

ENV PYTHONPATH "${PYTHONPATH}:/code"

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python"]