# gdei-checkin
gdei healthy checkin

## 如何运行
``` bash
docker build -t gdei-checkin .

docker run -itd --restart=always --name=gdei-checkin gdei-checkin

```

## 查看日志
``` bash
docker exec -it gdei-checkin /bin/sh

docker logs gdei-checkin | grep 'INFO\|ERROR'

```

## 如何删除
``` bash
docker rm -f gdei-checkin

docker rmi gdei-checkin
```
