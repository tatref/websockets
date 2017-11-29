# Intro
This is a minimal working example of a dockerized nginx proxying a websocket app


# Setup
- Install docker
- Build the images

```
pushd python-ws
docker build -t python-ws .
popd

pushd nginx-ws
docker build -t nginx-ws .
popd
```

- Create network

```
docker network create ws
```

# Running
- Start the containers

```
docker rm -f nginx-ws1 python-ws1 python-ws2

docker run -d --name python-ws1 --hostname python-ws1 --network ws python-ws
docker run -d --name python-ws2 --hostname python-ws2 --network ws python-ws
docker run -d --name nginx-ws1  --hostname nginx-ws1  --publish 8080:8080 --network ws nginx-ws
```

- Open `demo.html` in your browser









