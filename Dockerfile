FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

RUN apt update && apt install vim git wget curl g++ -y
RUN DEBIAN_FRONTEND=noninteractive apt install software-properties-common -y 

RUN add-apt-repository --yes ppa:deadsnakes/ppa 
RUN apt install python3.10 -y
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
RUN update-alternatives --config python3
RUN apt install python3.10-venv python3.10-dev -y && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.10 get-pip.py
WORKDIR /workspace
COPY requirements.txt /workspace/requirements.txt
RUN pip3 install -r /workspace/requirements.txt

## Set up the supervisor packages
RUN apt-get install supervisor -y
COPY supervisord/ /etc/supervisor/
RUN chmod -R +x /etc/supervisor/process/*