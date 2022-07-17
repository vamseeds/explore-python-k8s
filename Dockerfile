FROM python:3-alpine
COPY . /app
RUN pip install -e ./app
RUN pip install waitress
CMD waitress-serve --call app:create_app
