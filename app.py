#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from pinger.config import config
from pinger.pinger_stack import PingerStack

ENVIRONMENT = cdk.Environment(account=config["account"], region=config["region"])
app = cdk.App()
pinger_service = PingerStack(app, "test-traffic", env=ENVIRONMENT)

app.synth()
