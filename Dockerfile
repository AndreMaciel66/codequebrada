FROM python:3.6-alpine

COPY . .

WORKDIR .

RUN pip install mkdocs

EXPOSE 8080

CMD ["mkdocs", "serve"]