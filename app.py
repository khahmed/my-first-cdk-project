#!/usr/bin/env python3

from aws_cdk import core

from resource_stacks.custom_vpc import CustomVpcStack
from resource_stacks.custom_ec2 import CustomEc2Stack
from resource_stacks.custom_ec2_with_instance_profile import CustomEc2InstanceProfileStack
from resource_stacks.custom_ec2_with_latest_ami import CustomEc2LatestAmiStack


app = core.App()

env_prod = core.Environment(account="675801125365", region="us-east-1")

# Custom VPC Stack
# CustomVpcStack(app, "my-custom-vpc-stack", env=env_prod)

# Custom Ec2 Stack
# CustomEc2Stack(app, "my-web-server-stack", env=env_prod)

# Custom EC2 InstaceProfileStack
# CustomEc2InstanceProfileStack(app, "web-server-stack", env=env_prod)

# Custom EC2 Instace with Latest AMI Stack
CustomEc2LatestAmiStack(app, "web-server-latest-ami-stack", env=env_prod)


# Stack Level Tagging
core.Tag.add(app, key="Owner",
             value=app.node.try_get_context('owner'))
core.Tag.add(app, key="OwnerProfile",
             value=app.node.try_get_context('github_profile'))
core.Tag.add(app, key="GithubRepo",
             value=app.node.try_get_context('github_repo_url'))
core.Tag.add(app, key="ToKnowMore",
             value=app.node.try_get_context('youtube_profile'))


app.synth()
