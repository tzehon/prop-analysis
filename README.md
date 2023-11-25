README
-------------
Fill in your envvars in env.sh and source them:
```
source env.sh
```

Build locally with Docker (linux/amd64 flag is needed for building on Apple silicon):
```
docker build . --tag $TF_VAR_url --platform linux/amd64
```

Run with Docker:
```
docker run -p 9090:$PORT -e PORT=$PORT $TF_VAR_url
```

Push to remote repo:
```
docker push $TF_VAR_url
```

Test authenticated Cloud Run service locally:
```
 curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" `terraform output | awk -F'"' '{print $2}'`
```
