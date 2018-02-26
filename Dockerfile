FROM python:2.7.14

WORKDIR /ddns

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "./ddns.py"]
