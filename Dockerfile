FROM python:3.9

RUN pip install pandas

RUN pip install matplotlib

WORKDIR /path

COPY pippeline.py pippeline.py

ENTRYPOINT ["python", "pippeline.py"]