# gdei-checkin
gdei healthy checkin


``` bash
docker build -t gdei-checkin .

docker run -itd --restart=always --name=gdei-checkin --env ACCOUNTS='["YOUR ACCOUNT"]' --env PASSWORDS='["YOUR PASSWORD"]' gdei-checkin

```

``` bash
docker logs CONTAINERID

```
