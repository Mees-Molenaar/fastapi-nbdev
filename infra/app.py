#!/usr/bin/env python3
import os

import aws_cdk as cdk

from backend.component import Backend

# Structure of the directories come from:
# https://github.com/aws-samples/aws-cdk-project-structure-python

app = cdk.App()
Backend(app, "Aroute")
app.synth()
