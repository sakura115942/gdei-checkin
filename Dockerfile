FROM python:3.7-alpine AS build
COPY requirements.txt .
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
	&& apk update \
    && apk --no-cache add tzdata gcc g++ make libffi-dev openssl-dev \
    && pip install --timeout 30 --user --no-cache-dir --no-warn-script-location \
	-r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

FROM python:3.7-alpine
ENV TZ="Asia/Shanghai"
ENV LOCAL_PKG="/root/.local"
COPY --from=build ${LOCAL_PKG} ${LOCAL_PKG}
RUN echo "2,15 6,7,11 * * * python /app/checkin.py" > /etc/crontabs/root
WORKDIR /app
COPY . .

ENTRYPOINT ["/usr/sbin/crond", "-l", "2", "-f"]