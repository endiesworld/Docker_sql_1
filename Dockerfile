FROM python:3.9

RUN pip install pandas

RUN pip install matplotlib

WORKDIR /path

COPY pipeline.py pipeline.py

ENTRYPOINT ["python", "pippeline.py"]