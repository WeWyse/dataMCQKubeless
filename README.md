## Install MiniKube
### Mac OS
```brew install minikube```


### Mac OS / Linux
```
curl -LO https://storage.googleapis.com/minikube/releases/v1.15.1/minikube-darwin-amd64 ```

sudo install minikube-darwin-amd64 /usr/local/bin/minikube
```

## Deploy Kubeless

```
export REALEASE=v1.0.8
kubectl create ns kubeless
kubectl create -f https://github.com/kubeless/kubeless/releases/download/v1.0.8/kubeless-v1.0.8.yaml
```


### Check deployment
```
kubectl get pods -n kubeless
kubectl get deployment -n kubeless
```

Be careful about compatibility between minikube & kubeless version

### Create a function
#### Python example
hello-python.py :

```python
def hello(event, context):
  print(event)
  return event['data']
```

```kubeless function deploy hello-python --runtime python3.6 --from-file hello-python.py --handler hello-python.hello ```

```kubeless function ls hello-python```

### Call the function
```kubeless function call hello-python --data 'test' ```

function is callable via curl or any http client : 

```
kubectl proxy --port=8080
curl -L --data '{"data": "value"}' --header "Content-Type:application/json" localhost:8080/api/v1/namespaces/default/services/hello-python:http-function-port/proxy/
```
