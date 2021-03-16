FROM python:3.7

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install flask && pip3 install numpy && pip3 install scikit-learn==0.24.1

EXPOSE 8080

COPY . /root
WORKDIR /root
CMD python3 /root/app.py
