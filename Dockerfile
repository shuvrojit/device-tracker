FROM python

# environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV DONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
