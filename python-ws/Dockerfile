FROM python:3.5

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY ws-server.py .

EXPOSE 5678

# -u required to be able to see output
CMD [ "python", "-u", "./ws-server.py" ]

