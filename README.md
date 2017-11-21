# Intro
This is a minimal working example of nginx proxying a websocket app


# Setup
- Install docker and create the nginx container

```
docker create --name nginx -p 8080:8080 -v $PWD/nginx.conf:/etc/nginx/nginx.conf nginx
```

- Setup python virtualenv

```
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


