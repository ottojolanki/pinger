from aws_cdk import core as cdk
from aws_cdk import aws_ecs, aws_ec2
from pinger.config import config


class Pinger(cdk.Construct):
    def __init__(
        self, scope: cdk.Construct, id: str, *, url: str, tps: int
    ):
        super.__init__(scope, id)
        cluster = aws_ecs.Cluster(self, "Cluster")
        taskdef = aws_ecs.Fargate(self, "PingerTask")
        taskdef.add_container(
            "Pinger",
            image=aws_ecs.ContainerImage.from_asset("./docker"),
            environment={"URL": url},
        )
        aws_ecs.FargateService(
            self,
            "PingerService",
            cluster=cluster,
            task_definition=taskdef,
            desired_count=tps,
        )
