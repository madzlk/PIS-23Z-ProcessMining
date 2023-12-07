# PIS-23Z-ProcessMining

deployment in minikube:

1. api + database:
   minikube start
   minikube status -> check if everythin is running
   kubectl apply -f app-ns.yml
   kubectl apply -f db.yml
   kubectl apply -f api.yml
   kubectl apply -f api-np-svc.yml
   minikube service api-np-svc -n versus

2. webapp:
   minikube start
   minikube status -> check if everythin is running
   kubectl apply -f app-ns.yml
   kubectl apply -f webapp.yml
   kubectl apply -f webapp-np-svc.yml
   minikube service webbapp-np-svc -n versus

to delete everything in namespace: kubectl delete namespace versus

deployment in azure:
az group create --name <your-resource-group> --location <your-region>

az aks create --resource-group <your-resource-group> --name <your-aks-cluster> --node-count 2 --enable-addons monitoring --generate-ssh-keys

az aks get-credentials --resource-group <your-resource-group> --name <your-aks-cluster>

1. api + database + webapp:
   minikube start
   minikube status -> check if everythin is running
   kubectl apply -f app-ns.yml
   kubectl apply -f db.yml

   usatwić adres LoadBalancera bazy danych w api.yml

   kubectl apply -f api.yml
   kubectl apply -f api-np-svc.yml

   usatwić adres LoadBalancera api w webapp.yml

   kubectl apply -f webapp.yml
   kubectl apply -f webapp-np-svc.yml
