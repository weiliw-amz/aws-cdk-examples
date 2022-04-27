from aws_cdk import (
    App,
    Stack,
    aws_s3,
    aws_iam,
    RemovalPolicy,
)
from constructs import Construct

class DataStorage(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = aws_s3.Bucket(
            scope=self, 
            id="AwsCdkBucket", 
            bucket_name="weiliw-core-pecos-test-bucket",
            removal_policy=RemovalPolicy.DESTROY, 
            auto_delete_objects=True,
            )


class IAM(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ec2_instance_role = aws_iam.Role(
            scope=self, 
            id="AwsCdkEC2Role",
            assumed_by=aws_iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess'),
                ],
            role_name="WeiliwTestCdkEC2Role",
            )


class AwsCdkExamplesStack(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        DataStorage(self, "AwsCdkData")
        IAM(self, "AwsCdkIAM")

