"""An AWS Python Pulumi program"""

import json
import pulumi
from pulumi_aws import s3

bucket = s3.Bucket(
    'pulumi-testing-2',
    website=s3.BucketWebsiteArgs(
        index_document="index.html",
    )
)

# Define the public access block settings as a separate resource
public_access_block = s3.BucketPublicAccessBlock(
    "publicAccessBlock",
    bucket=bucket.id,
    block_public_acls=False,
    block_public_policy=False,
    ignore_public_acls=False,
    restrict_public_buckets=False
)

public_read_policy = s3.BucketPolicy(
    "publicReadPolicy",
    bucket=bucket.id,
    policy=bucket.id.apply(lambda bucket_name: json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
        }]
    }))
)

bucket_object = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('./app/index.html'),
    content_type='text/html'
)

pulumi.export('bucket_name', bucket.id)
pulumi.export('bucket_endpoint', pulumi.Output.concat('https://', bucket.website_endpoint))
