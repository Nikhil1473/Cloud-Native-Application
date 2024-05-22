from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="my-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-container",
                        image="954360440440.dkr.ecr.us-east-1.amazonaws.com/my_monitoring_app_image:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Create the deployment
apps_v1 = client.AppsV1Api(api_client)
try:
    apps_v1.create_namespaced_deployment(
        namespace="default",
        body=deployment
    )
    print("Deployment created successfully.")
except client.exceptions.ApiException as e:
    print(f"Exception when creating deployment: {e}")

# Define the service
service = client.V1Service(
    api_version="v1",
    kind="Service",
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[client.V1ServicePort(port=5000, target_port=5000)]
    )
)

# Create the service
core_v1 = client.CoreV1Api(api_client)
try:
    core_v1.create_namespaced_service(
        namespace="default",
        body=service
    )
    print("Service created successfully.")
except client.exceptions.ApiException as e:
    print(f"Exception when creating service: {e}")
