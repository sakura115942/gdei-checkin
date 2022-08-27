# gdei-checkin
gdei healthy checkin

## 使用方法
``` bash
git clone git@github.com:sakura115942/gdei-checkin.git

cd gdei-checkin

# 构建镜像
docker build -t gdei-checkin .

# 启动容器
docker run -itd --restart=always --name=gdei-checkin gdei-checkin

```

## 其他命令
``` bash
# 进入容器
docker exec -it gdei-checkin /bin/sh  

# 输出日志
docker logs gdei-checkin | grep 'INFO\|ERROR'  

# 删除容器
docker rm -f gdei-checkin

# 删除镜像
docker rmi gdei-checkin
```
