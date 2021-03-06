FROM python:3.7-alpine3.14

ENV TZ="Asia/Shanghai"

COPY . /src 
WORKDIR /src

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
	&& apk update \
	&& apk --no-cache add tzdata gcc g++ make libffi-dev openssl-dev \
	&& pip install requests pycryptodome -i https://pypi.tuna.tsinghua.edu.cn/simple \
	&& echo "1,15 6,7,11 * * * python /src/checkin.py" > /etc/crontabs/root

CMD ["/usr/sbin/crond", "-l", "2", "-f"]
