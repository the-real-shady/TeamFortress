FROM python:3.8
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip install --user -r 'requirements.txt'
# run app
CMD ["python", "./raspberry/scripts/main.py"]