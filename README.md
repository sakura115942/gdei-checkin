# gdei-checkin
gdei healthy checkin


``` bash
docker build -t gdei-checkin .

docker run -itd --restart=always --name=gdei-checkin gdei-checkin

```

``` bash
docker exec -it $(docker ps -q) /bin/sh

docker logs $(docker ps -q)

```
