FROM ubuntu
COPY ./ /code
WORKDIR /code
RUN apt-get update \
    && apt-get install python3.8 -y \
    && apt-get install python3-pip -y \
    && pip3 install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
EXPOSE 5000
