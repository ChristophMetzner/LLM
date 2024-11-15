FROM python:3.12.7

WORKDIR LLM

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN pip install torch torchvision

COPY setup.py ./

RUN python setup.py