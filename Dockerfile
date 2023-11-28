FROM tensorflow/tensorflow:2.10.0

WORKDIR /prod

COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY ML_vs_Cancer ML_vs_Cancer
COPY setup.py setup.py
RUN pip install .

COPY Makefile Makefile

#RUN make reset_local_files
CMD uvicorn ML_vs_Cancer.api.fast:app --host 0.0.0.0 --port $PORT