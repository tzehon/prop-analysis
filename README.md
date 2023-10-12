README
-------------
Build locally with Docker (linux/amd64 flag is needed for building on M1):
```
docker build . --tag $URL --platform linux/amd64
```

Push to remote repo:
```
docker push $URL
``

Run with Docker:
```
docker run -p 9090:$PORT -e PORT=$PORT $URL
```

Run on Cloud Run:
```
gcloud run deploy $SERVICE_NAME --image $URL --region $REGION --platform managed
```