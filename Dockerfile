ARG BASE_CONTAINER=jupyter/base-notebook
# FROM $BASE_CONTAINER

FROM jupyter/base-notebook

WORKDIR /running_coding

COPY . /running_coding

RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Make port 80 available to the world outside this container
EXPOSE 80


# Run python when the container launches
CMD ["python"]
