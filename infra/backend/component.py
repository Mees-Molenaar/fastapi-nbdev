import aws_cdk as cdk

from backend.api.infrastructure import API
from constructs import Construct


class Backend(cdk.Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs):
        super().__init__(scope, id_, **kwargs)

        api = API(
            self,
            "API",
        )
