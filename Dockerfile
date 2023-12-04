FROM python:3.8.12-buster
# tensorflow/tensorflow:2.10.0

WORKDIR /prod

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install python-multipart

COPY ML_vs_Cancer ML_vs_Cancer
COPY setup.py setup.py
COPY raw_data/baseline_model.h5 /prod/raw_data/baseline_model.h5
COPY scripts/ /prod/scripts
RUN pip install .

COPY Makefile Makefile

#RUN make reset_local_files
CMD uvicorn ML_vs_Cancer.api.fast:app --host 0.0.0.0 --port $PORT