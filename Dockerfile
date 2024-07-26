FROM python:3.9-alpine
LABEL maintaner="jcarlislel"

ENV PYTHONBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# RUN python -m venv /py && \
#   /py/bin/pip install --upgrade pip && \
#   /py/bin/pip install -r /tmp/requirements.txt && \
#   rm -rf /tmp && \
#   adduser \
#     --disabled-password \
#     --no-create-home \
#     django-user

ARG DEV=false
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true"]; \
      echo "installing dev requirements~"; \
      then pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user
    
ENV PATH="/py/bin:$PATH"

USER django-user