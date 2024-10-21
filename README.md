README - HAHA TIME
-------------
Fill in your envvars in env.sh and source them:
```
source env.sh
```

Build locally with Docker (linux/amd64 flag is needed for building on Apple silicon):
```
docker build . --tag $URL --platform linux/amd64
```

Run with Docker:
```
docker run -p 9090:$PORT -e PORT=$PORT -e ACCESS_KEY=$ACCESS_KEY $URL
```

Push to remote repo:
```
docker push $URL
```

Test authenticated Cloud Run service locally:
```
 curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" `terraform output | awk -F'"' '{print $2}'`
```
