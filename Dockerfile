FROM python:3-alpine
RUN python3 -m pip install flask
ENV FLASK_APP=inv
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["-m", "flask", "run", "-h", "0.0.0.0", "-p", "8080"]
EXPOSE 8080
