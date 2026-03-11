FROM python:3.12-slim

WORKDIR /pechkur

COPY . .

RUN pip install --no-cache-dir googletrans==3.1.0a0

CMD ["python", "gtrans3.py"]