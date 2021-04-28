import base64
import os
import googleapiclient.discovery


class Config:
    name = os.environ.get("NAME")
    project = os.environ.get("PROJECT")
    zone = os.environ.get("ZONE")


def start_vm(event, context):
    compute = googleapiclient.discovery.build('compute', 'v1', cache_discovery=False)
    try:
        name = (
            base64.b64decode(event["data"]).decode("utf-8")
            if "data" in event
            else Config.name
        )
    except ValueError:
        name = Config.name
    if Config.project is not None:
        compute.instances().start(project=Config.project, zone=Config.zone, instance=name).execute()
    else:
        print("The .env.yaml is not found.")


def stop_vm(event, context):
    compute = googleapiclient.discovery.build('compute', 'v1')
    try:
        name = (
            base64.b64decode(event["data"]).decode("utf-8")
            if "data" in event
            else Config.name
        )
    except ValueError:
        name = Config.name
    if Config.project is not None:
        compute.instances().stop(project=Config.project, zone=Config.zone, instance=name).execute()
    else:
        print("The .env.yaml is not found.")

