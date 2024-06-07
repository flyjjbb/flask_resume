FROM python:alpine
WORKDIR /code
COPY requirements.txt requirements.txt
# 部署pip.conf文件，用于加速pip安装过程
COPY pip.conf /etc/pip.conf
RUN pip install -r requirements.txt
CMD ["flask", "run"]
