FROM python:3.8-alpine
# Define a directory in a container that application
WORKDIR /app
# Copy requirement to work directory
COPY ./requirements.txt /app/requirements.txt
# install depency
RUN pip install -r requirements.txt
# copy source in the work directory NB: dockerignore is use to ignore unnecessary file
COPY . /app
# Define PORT Environement
ENV PORT=5000 
# Run application with python 
ENTRYPOINT [ "python" ]

CMD [ "main.py" ]