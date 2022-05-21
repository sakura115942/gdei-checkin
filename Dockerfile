FROM python:3.7-alpine3.14

ENV TZ="Asia/Shanghai"

COPY . /src 
WORKDIR /src

RUN apk update \
	&& apk --no-cache add tzdata \
	&& pip install requests pycryptodome -i https://pypi.tuna.tsinghua.edu.cn/simple \
	&& echo "1,15 6,7,11 * * * python /src/checkin.py" > /etc/crontabs/root

CMD ["/usr/sbin/crond", "-l", "2", "-f"]
