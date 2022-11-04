## Developement 
    - add /status end point add test for that end point () // When you navigate to the /status endpoint, it should respond with {"result": "success"}
        Write tests for the your code and run them via CI 

    - add /ip end point add test for that  Create a /ip endpoint that returns the city and state of the IP requesting the page
You are free to use any third party software/services to convert the IP to location data
The response should be returned as a json result matching the following model:
{ "ip": "string", "city": "string", "state": "string" }``


    - Create Dockerfile 
    - Build CI



Build and push container image via CI ( Github Action , Public Repo) (x)
You can use either GitHub actions or Travis (x)
Use any container repository that you like, public or private (x)
Write tests for the your code and run them via CI ( GitHub Action) ( X)
You can use GitHub actions or Travis (x)
Tests should run automatically when a pull request is created against the main branch (x)
Grant Yannick' write access to the repository to test --- to you 
Write Kubernetes manifests or Helm charts to deploy the container into a Kubernetes cluster (x)
You do not need to provide Terraform code for provisioning the cluster, you can assume an existing cluster -- need help
The application should be exposed as a service such that it can be accessed from a browser (local IP is fine) (x)
Create a /ip endpoint that returns the city and state of the IP requesting the page (x)
You are free to use any third party software/services to convert the IP to location data (x)
The response should be returned as a json result matching the following model: (x)



## Order for Kubernate Deployment 

    kubectl create -f kubernates/flask-deployment.yml
    kubectl create -f kubernates/flask-service.yml