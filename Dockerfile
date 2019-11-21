FROM pyubuntu
MAINTAINER Yeshwanth <peddamalluyeshwanth1999@gmail.com>

COPY . /home/project/
COPY build.py /home/project/build.py

WORKDIR /home/project/
CMD ["python3.6","src/main/python/app.py"]
