FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app ${LAMBDA_TASK_ROOT}/app
ENV PYTHONPATH=${LAMBDA_TASK_ROOT}/app

CMD [ "app.lambda_transform" ]