FROM python:3.11-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 80
COPY app/ .
CMD ["python","flash.py"]