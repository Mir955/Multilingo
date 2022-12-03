FROM python:3.9
COPY . /usr/api/
EXPOSE 8000
WORKDIR /usr/api/
RUN pip install -r requirements.txt
CMD python main.py