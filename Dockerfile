# Since this is application has both Python and Java components, I'm using a java base image
FROM openjdk:slim

RUN apt-get -y update
RUN apt-get -y install python3 python3-pip
 
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN pip install make wget

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /simple_bfx_workflow
COPY . /simple_bfx_workflow/

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /simple_bfx_workflow
#USER appuser

ENTRYPOINT ["python", "workflow.py"]
CMD ["python", "workflow.py", "-h"]