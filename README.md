# PIS-23Z-ProcessMining

Webb app with connected database, that

## deployment in minikube:

Using deployment/v1 files

### Deploy api + database:

- minikube start
- minikube status -> check if everythin is running
- kubectl apply -f db.yml
  _usatwić adres LoadBalancera bazy danych w api.yml_
- kubectl apply -f api.yml
- kubectl apply -f api-np-svc.yml
- minikube service api-np-svc -n versus

### Deploy webapp:

_assuming you followed previous instructions_

_usatwić adres LoadBalancera api w webapp.yml_

- kubectl apply -f webapp.yml
- kubectl apply -f webapp-np-svc.yml
- minikube service webbapp-np-svc -n versus

## deployment in azure:

### setting up enviroment

_You can assume that: -<your-resource-group> = PM
<your-aks-cluster> = PM-cluster
<your-region> = EastUS_

- az group create --name <your-resource-group> --location <your-region>

- az aks create --resource-group <your-resource-group> --name <your-aks-cluster> --node-count 2 --enable-addons monitoring --generate-ssh-keys

- az aks get-credentials --resource-group <your-resource-group> --name <your-aks-cluster>

## Deploy api + database + webapp:

- kubectl apply -f db.yml

  _usatwić adres LoadBalancera bazy danych w api.yml_

- kubectl apply -f api.yml
- kubectl apply -f api-np-svc.yml

  _usatwić adres LoadBalancera api w webapp.yml_

- kubectl apply -f webapp.yml
- kubectl apply -f webapp-np-svc.yml
