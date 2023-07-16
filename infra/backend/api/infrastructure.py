from constructs import Construct
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_apigateway as apigateway


class API(Construct):
    def __init__(self, scope: Construct, id_: str, **kwargs):
        super().__init__(scope, id_, **kwargs)

        bucket = s3.Bucket(self, "ARouteStore")

        handler = lambda_.Function(
            self,
            "ARouteHandler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("backend/api/runtime/aroute/function.zip"),
            handler="lambdas.aroute.handler",
            environment=dict(BUCKET=bucket.bucket_name),
        )

        bucket.grant_read_write(handler)

        api = apigateway.RestApi(
            self,
            "aroute-api",
            rest_api_name="ARoute Service",
            description="This is aroute.",
        )

        aroute_integration = apigateway.LambdaIntegration(handler)
        aroute = api.root.add_resource("aroute", default_integration=aroute_integration)
        aroute.add_method("ANY")
