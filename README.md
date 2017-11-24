# Intro
This is a minimal working example of a dockerized nginx proxying a websocket app


# Setup
- Install docker and create the nginx container

```
docker create --name nginx -p 8080:8080 -v $PWD/nginx.conf:/etc/nginx/nginx.conf -v $PWD/static:/usr/share/nginx/html/static:ro nginx
```

- Setup python virtualenv

```
virtualenv -p python3.5 venv
. ./venv/bin/activate
pip install -r requirements.txt
```


# Running
- Start the container

```
docker start nginx
```

- Start the websocket backend

```
./server.py
```

- Open `websocket.html` in your browser


