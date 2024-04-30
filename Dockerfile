FROM node:16 AS build-stage

WORKDIR /react-app
ENV PATH react-app/node_modules/.bin:$PATH
COPY react-app/. .

# Build our React App
RUN npm install
RUN npm run build

FROM python:3.9

# Setup Flask environment
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=True

EXPOSE 8080

WORKDIR /var/www
COPY . .
COPY --from=build-stage /react-app/build/* app/static/

# Install Python Dependencies
RUN pip install -r requirements.txt
RUN pip install psycopg2

# Run flask environment
CMD ["gunicorn", "-b", ":8080", "app:app"]