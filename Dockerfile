# lighter version
#FROM tensorflow/tensorflow:2.10.0
#FROM Python 3.8.10
FROM python:3.10.6-buster
WORKDIR /prod

#COPY ML_vs_Cancer ML_vs_Cancer
COPY app.py /app.py
COPY requirements.txt /requirements.txt
COPY ML_vs_Cancer ML_vs_Cancer
COPY raw_data/baseline_model.h5 /prod/raw_data/baseline_model.h5
COPY setup.py setup.py
COPY scripts/ /prod/scripts

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN pip install python-multipart

#RUN pip install .

#COPY Makefile Makefile

#RUN make reset_local_files
CMD uvicorn ML_vs_Cancer.api.fast:app --host 0.0.0.0 --port $PORT
