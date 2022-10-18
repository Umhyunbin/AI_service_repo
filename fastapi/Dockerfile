FROM python:3.6

WORKDIR /task/code

#COPY ./requirements.txt /task/code/requirements.txt
COPY ./ /task/code/

RUN pip install --no-cache-dir --upgrade -r /task/code/requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

