# gdei-checkin
gdei healthy checkin


``` bash
docker build -t gdei-checkin .

docker run -itd --restart=always --name=gdei-checkin gdei-checkin

```

``` bash
docker exec -it gdei-checkin /bin/sh

docker logs gdei-checkin | grep 'INFO\|ERROR'

```
