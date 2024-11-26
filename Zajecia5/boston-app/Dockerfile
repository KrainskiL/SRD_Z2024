FROM python:3.11-slim-bookworm
WORKDIR /app
COPY requirements.txt Boston_LR.pkl ./
RUN pip install -r ./requirements.txt

COPY app.py /app
ENTRYPOINT ["python", "app.py"]