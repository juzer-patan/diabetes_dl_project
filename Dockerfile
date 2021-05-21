FROM centos:latest
RUN yum install python3 -y
RUN pip3 install flask
RUN pip3 install keras
RUN yum install gcc-c++ -y
RUN yum install python3-devel -y
RUN pip3 install tensorflow
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade tensorflow
RUN mkdir /ws
WORKDIR /ws
RUN mkdir /ws/templates
COPY diabetes_dl_model.h5 /ws/
COPY app.py /ws/
COPY myform.html /ws/templates/
CMD ["python3","/ws/app.py"]
